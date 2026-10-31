"""Offline supervised typed BILOU extraction with hashed lexical/context features.

No source IDs, reference files, scorer or external service is consulted. Reusable
baseline, not a claim of state-of-the-art Spanish extraction. Per-type heads allow
overlapping different labels. Same-type token conflicts use a documented shortest
span projection for fitting only; evaluation references are never projected.
"""
import argparse
import csv
import json
import re
import time
from pathlib import Path
import numpy as np
from sklearn.feature_extraction import FeatureHasher
from sklearn.linear_model import SGDClassifier
from scipy.special import softmax

LABELS = ('WHAT', 'WHEN', 'WHERE', 'WHO', 'WHY', 'HOW')
STATES = ('O', 'B', 'I', 'L', 'U')
TOKEN = re.compile(r'\w+|[^\w\s]', re.UNICODE)


def read_rows(p, labeled):
    with Path(p).open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    if labeled:
        for r in rows:
            r['TAGS'] = json.loads(r['TAGS'])
    return rows


def tokens(text):
    return [(m.group(), m.start(), m.end()) for m in TOKEN.finditer(text)]


def features(ts):
    out = []
    for i, (word, a, b) in enumerate(ts):
        d = {'bias': 1., 'upper': float(word.isupper()), 'title': float(word.istitle()),
             'digit': float(word.isdigit()), 'length': min(len(word), 20) / 20}
        for shift in (-2, -1, 0, 1, 2):
            j = i + shift
            w = ts[j][0] if 0 <= j < len(ts) else '<EDGE>'
            low = w.lower()
            d[f'w{shift}={low}'] = 1.
            d[f'shape{shift}=' + re.sub('[a-záéíóúñü]', 'x', re.sub('[A-ZÁÉÍÓÚÑÜ]', 'X', w))] = 1.
            for n in (1, 2, 3, 4):
                d[f'prefix{shift},{n}={low[:n]}'] = 1.
                d[f'suffix{shift},{n}={low[-n:]}'] = 1.
        if i:
            d['bigram=' + ts[i-1][0].lower() + '|' + word.lower()] = 1.
        out.append(d)
    return out


def target_states(row, ts, label):
    y = np.zeros(len(ts), dtype=np.int32)
    used = set()
    projected = 0
    candidates = sorted((t for t in row['TAGS'] if t['tag'] == label),
                        key=lambda t: (t['end']-t['start'], t['start'], t['end']))
    for t in candidates:
        indices = [i for i, (_, a, b) in enumerate(ts) if a < t['end'] and b > t['start']]
        if not indices or any(i in used for i in indices):
            projected += 1
            continue
        used.update(indices)
        if len(indices) == 1:
            y[indices[0]] = 4
        else:
            y[indices[0]], y[indices[-1]] = 1, 3
            y[indices[1:-1]] = 2
    return y, projected


def design(rows, hasher):
    token_lists = [tokens(r['TEXT']) for r in rows]
    flat = [d for ts in token_lists for d in features(ts)]
    return token_lists, hasher.transform(flat)


def fit(rows, alpha=1e-5, balanced=False):
    hasher = FeatureHasher(n_features=2**18, input_type='dict', alternate_sign=False)
    ts, x = design(rows, hasher)
    models, conflicts = [], {}
    for label in LABELS:
        pairs = [target_states(r, t, label) for r, t in zip(rows, ts)]
        y = np.concatenate([v[0] for v in pairs])
        conflicts[label] = sum(v[1] for v in pairs)
        model = SGDClassifier(loss='log_loss', alpha=alpha, max_iter=40, tol=1e-4,
                              random_state=2026, class_weight='balanced' if balanced else None,
                              average=True, n_jobs=1)
        model.fit(x, y)
        models.append(model)
    return hasher, models, conflicts


def probabilities(model, rows):
    hasher, models, _ = model
    ts, x = design(rows, hasher)
    lengths = [len(t) for t in ts]
    by_label = []
    for m in models:
        probabilities = np.full((x.shape[0], 5), 1e-12)
        fitted = m.predict_proba(x)
        for column, state in enumerate(m.classes_):
            probabilities[:, state] = fitted[:, column]
        by_label.append(probabilities)
    outputs, cursor = [], 0
    for n in lengths:
        outputs.append([p[cursor:cursor+n] for p in by_label])
        cursor += n
    return ts, outputs


def decode(ts, probabilities, penalty=0.0):
    n = len(ts)
    if not n:
        return []
    # BILOU transitions. Entity-start penalty tunes inclusion, not raw spans.
    allowed = np.full((5, 5), -np.inf)
    for a in (0, 3, 4):
        allowed[a, [0, 1, 4]] = 0
    for a in (1, 2):
        allowed[a, [2, 3]] = 0
    emission = np.log(np.maximum(probabilities, 1e-12))
    emission[:, [1, 4]] -= penalty
    score = np.full((n, 5), -np.inf)
    back = np.zeros((n, 5), dtype=int)
    score[0, [0, 1, 4]] = emission[0, [0, 1, 4]]
    for i in range(1, n):
        candidate = score[i-1, :, None] + allowed
        back[i] = np.argmax(candidate, axis=0)
        score[i] = candidate[back[i], np.arange(5)] + emission[i]
    state = max((0, 3, 4), key=lambda j: score[-1, j])
    path = [state]
    for i in range(n-1, 0, -1):
        state = int(back[i, state])
        path.append(state)
    path.reverse()
    spans, start = [], None
    for i, state in enumerate(path):
        if state == 4:
            spans.append((ts[i][1], ts[i][2]))
        elif state == 1:
            start = ts[i][1]
        elif state == 3 and start is not None:
            spans.append((start, ts[i][2]))
            start = None
    return spans


def predictions(rows, token_lists, probs, penalty=0.):
    out = []
    for row, ts, heads in zip(rows, token_lists, probs):
        tags = []
        for label, head in zip(LABELS, heads):
            tags.extend({'start': a, 'end': b, 'tag': label} for a, b in decode(ts, head, penalty))
        tags.sort(key=lambda t: (t['start'], t['tag'], t['end']))
        out.append({'ID': row['ID'], 'TEXT': row['TEXT'], 'TAGS': tags})
    return out


def write(p, rows):
    with Path(p).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, ['ID', 'TEXT', 'TAGS'], lineterminator='\n')
        w.writeheader()
        for row in rows:
            w.writerow({**row, 'TAGS': json.dumps(row['TAGS'], ensure_ascii=False)})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--train', required=True)
    p.add_argument('--inputs', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--alpha', type=float, default=1e-5)
    p.add_argument('--balanced', action='store_true')
    p.add_argument('--penalty', type=float, default=0.)
    a = p.parse_args()
    start = time.monotonic()
    model = fit(read_rows(a.train, True), a.alpha, a.balanced)
    rows = read_rows(a.inputs, False)
    ts, probs = probabilities(model, rows)
    write(a.output, predictions(rows, ts, probs, a.penalty))
    print(json.dumps({'seconds': time.monotonic()-start, 'rows': len(rows),
                      'training_projection_conflicts': model[2]}))


if __name__ == '__main__':
    main()
