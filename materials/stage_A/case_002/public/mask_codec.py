"""COCO column-major compressed RLE and polygon rasterization.

Polygon and compressed-count algorithms adapted from Microsoft COCO Toolbox 2.0,
Copyright (c) 2014, Piotr Dollar and Tsung-Yi Lin. Simplified BSD License;
see COCO-LICENSE.txt. This module contains format conversion only, no scorer.
"""
import math


def compress_counts(counts):
    output = []
    for i, value in enumerate(counts):
        x = value - counts[i - 2] if i > 2 else value
        while True:
            c = x & 31
            x >>= 5
            more = x != (-1 if c & 16 else 0)
            output.append(chr((c | (32 if more else 0)) + 48))
            if not more:
                break
    return ''.join(output)


def parse_counts(text, height=2048, width=2048):
    if not isinstance(text, str) or not text:
        raise ValueError('RLE counts must be a nonempty COCO ASCII string')
    counts, i, total = [], 0, 0
    n = height * width
    while i < len(text):
        x, k = 0, 0
        while True:
            if i >= len(text) or k > 8:
                raise ValueError('Truncated or oversized compressed count')
            c = ord(text[i]) - 48
            if not 0 <= c <= 63:
                raise ValueError('RLE contains a non-COCO character')
            x |= (c & 31) << (5 * k)
            i += 1
            k += 1
            if not c & 32:
                if c & 16:
                    x |= -1 << (5 * k)
                break
        if len(counts) > 2:
            x += counts[-2]
        if x < 0:
            raise ValueError('Negative run count')
        total += x
        if total > n or len(counts) > n + 1:
            raise ValueError('Run counts exceed the fixed pixel domain')
        counts.append(x)
    if total != n:
        raise ValueError('RLE pixel count differs from the fixed image size')
    if compress_counts(counts) != text:
        raise ValueError('Noncanonical compressed count representation')
    return counts


def foreground_runs(text, height=2048, width=2048):
    counts = parse_counts(text, height, width)
    runs, start = [], 0
    for i, length in enumerate(counts):
        if i % 2 and length:
            if runs and runs[-1][1] == start:
                runs[-1] = (runs[-1][0], start + length)
            else:
                runs.append((start, start + length))
        start += length
    return runs


def runs_to_rle(runs, height=2048, width=2048):
    n, end, counts = height * width, 0, []
    for start, stop in runs:
        if not isinstance(start, int) or not isinstance(stop, int) or start < end or stop <= start or stop > n:
            raise ValueError('Invalid foreground intervals')
        if counts and start == end:
            counts[-1] += stop - start
        else:
            counts.extend([start - end, stop - start])
        end = stop
    counts.append(n - end)
    return compress_counts(counts)


def encode(mask):
    import numpy as np
    a = np.asarray(mask)
    if a.ndim != 2 or not np.all((a == 0) | (a == 1)):
        raise ValueError('Expected a two-dimensional binary mask')
    flat = a.astype(bool).reshape(-1, order='F')
    edges = np.flatnonzero(np.diff(np.r_[False, flat, False].astype(np.int8)))
    return runs_to_rle([(int(s), int(e)) for s, e in zip(edges[::2], edges[1::2])], *a.shape)


def decode(text, height=2048, width=2048):
    import numpy as np
    flat = np.zeros(height * width, dtype=bool)
    for start, end in foreground_runs(text, height, width):
        flat[start:end] = True
    return flat.reshape(height, width, order='F')


def polygon_counts(xy, height=2048, width=2048):
    if len(xy) < 6 or len(xy) % 2 or any(not math.isfinite(v) for v in xy):
        raise ValueError('Invalid polygon')
    # Preserve C integer truncation and the upstream 5x boundary rasterization.
    x = [int(5 * v + .5) for v in xy[::2]]
    y = [int(5 * v + .5) for v in xy[1::2]]
    x.append(x[0]); y.append(y[0])
    u, v = [], []
    for j in range(len(x) - 1):
        xs, xe, ys, ye = x[j], x[j+1], y[j], y[j+1]
        dx, dy = abs(xe - xs), abs(ys - ye)
        flip = (dx >= dy and xs > xe) or (dx < dy and ys > ye)
        if flip:
            xs, xe, ys, ye = xe, xs, ye, ys
        slope = (ye - ys) / dx if dx >= dy and dx else ((xe - xs) / dy if dy else 0)
        for d in range(max(dx, dy) + 1):
            t = max(dx, dy) - d if flip else d
            u.append(t + xs if dx >= dy else int(xs + slope * t + .5))
            v.append(int(ys + slope * t + .5) if dx >= dy else t + ys)
    boundary = []
    for j in range(1, len(u)):
        if u[j] == u[j-1]:
            continue
        xd = ((u[j] if u[j] < u[j-1] else u[j] - 1) + .5) / 5 - .5
        if math.floor(xd) != xd or xd < 0 or xd > width - 1:
            continue
        yd = (min(v[j], v[j-1]) + .5) / 5 - .5
        boundary.append(int(xd) * height + math.ceil(max(0, min(height, yd))))
    boundary.append(height * width)
    boundary.sort()
    deltas, previous = [], 0
    for a in boundary:
        deltas.append(a - previous); previous = a
    counts, j = [deltas[0]], 1
    while j < len(deltas):
        if deltas[j] > 0:
            counts.append(deltas[j]); j += 1
        else:
            j += 1
            if j < len(deltas):
                counts[-1] += deltas[j]; j += 1
    return counts


def polygons_to_rle(polygons, height=2048, width=2048):
    runs = []
    for xy in polygons:
        runs.extend(foreground_runs(compress_counts(polygon_counts(xy, height, width)), height, width))
    merged = []
    for start, end in sorted(runs):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return runs_to_rle(merged, height, width)
