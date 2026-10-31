"""Shared age canonicalizer. Parsing only: no evaluation or matching policy.

Examples: 12M == 1Y; 30Y6M == 30.5Y; 31Y-72Y == 31-72 years.
Bare numerals and unsupported text are opaque; ranges are not averaged.
"""
from fractions import Fraction
import re

NULLS = {'', 'null', 'nan', 'not applicable', 'not available', 'not provided'}
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)'
UNIT = r'(?:years?|months?|weeks?|days?|y|m|w|d)'
ATOM = re.compile(r'('+NUMBER+r')\s*('+UNIT+r')', re.I)
FACTORS = {'y': Fraction(1), 'm': Fraction(1, 12), 'w': Fraction(28, 1461), 'd': Fraction(4, 1461)}
SHARED_RANGE = re.compile(r'^('+NUMBER+r')\s*(?:-|–|—|\bto(?![a-z]))\s*('+NUMBER+r')\s*('+UNIT+r')$', re.I)
NONFINITE = re.compile(r'^[+-]?(?:inf(?:inity)?|nan)\s*(?:'+UNIT+r')?$', re.I)


def normalize(value):
    if value is None: return ''
    if not isinstance(value, str): raise ValueError('Age values must be strings')
    return ' '.join(value.casefold().split())


def _scalar(text):
    matches = list(ATOM.finditer(text))
    if not matches: return None
    end = 0; values = []
    for match in matches:
        gap = text[end:match.start()].strip()
        if gap not in ['', '+']: return None
        values.append((Fraction(match[1]), match[2][0].lower()))
        end = match.end()
    if text[end:].strip(): return None
    if any(v < 0 for v, _ in values): raise ValueError('Negative parsed ages are invalid')
    return sum((v*FACTORS[u] for v, u in values), Fraction(0))


def parse_age(value):
    """Return None, ('interval', Fraction lower, Fraction upper), or ('opaque', text)."""
    text = normalize(value)
    if text in NULLS: return None
    # Recognize a true minus sign in otherwise explicit ages without rewriting opaque text.
    parsed_text = text.replace('−', '-')
    if NONFINITE.fullmatch(parsed_text): raise ValueError('Nonfinite parsed ages are invalid')
    special = r'[+-]?(?:inf(?:inity)?|nan)'
    if re.fullmatch(r'(?:(?:'+NUMBER+'|'+special+r')\s*'+UNIT+r'\s*\+?\s*)+',parsed_text,re.I) and re.search(r'nan|inf',parsed_text,re.I):
        raise ValueError('Nonfinite parsed age component')
    shared = SHARED_RANGE.fullmatch(parsed_text)
    if shared:
        a, b = Fraction(shared[1]), Fraction(shared[2]); factor = FACTORS[shared[3][0]]
        if min(a, b) < 0 or a > b: raise ValueError('Negative or reversed age range')
        return ('interval', a*factor, b*factor)
    for separator in re.finditer(r'-|–|—|\bto(?![a-z])', parsed_text):
        if separator.start() == 0: continue
        left, right = parsed_text[:separator.start()].strip(), parsed_text[separator.end():].strip()
        if (NONFINITE.fullmatch(left) and _scalar(right) is not None) or (NONFINITE.fullmatch(right) and _scalar(left) is not None):
            raise ValueError('Nonfinite age range endpoint')
        a, b = _scalar(left), _scalar(right)
        if a is not None and b is not None:
            if a > b: raise ValueError('Reversed age range')
            return ('interval', a, b)
    age = _scalar(parsed_text)
    if age is not None: return ('interval', age, age)
    return ('opaque', text)


def canonical_values(values):
    if not isinstance(values, list): raise ValueError('Prediction must be a JSON list of age strings')
    if len(values) > 10000: raise ValueError('Too many age values')
    output = {}
    for value in values:
        if not isinstance(value, str) or len(value) > 10000: raise ValueError('Age entries must be strings of at most10000 characters')
        key = parse_age(value)
        if key is not None: output.setdefault(key, normalize(value))
    return output
