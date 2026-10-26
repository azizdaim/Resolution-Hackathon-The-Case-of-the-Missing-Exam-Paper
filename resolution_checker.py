"""CS3081 resolution assignment: exhaustive semantic verification (Python stdlib)."""
from itertools import product

CLAUSES = {
    'K1': ('~D', 'S', 'O'), 'K2': ('D',),
    'K3': ('~S', 'C'), 'K4': ('~F', 'C'), 'K5': ('~C',),
    'K6': ('~L', 'Y'), 'K7': ('~Y', 'K'), 'K8': ('~K', 'Y'),
    'K9': ('~K', '~A'),
}
VARS = ('D', 'S', 'O', 'L', 'C', 'F', 'Y', 'K', 'A')

def literal_true(literal, assignment):
    return not assignment[literal[1:]] if literal.startswith('~') else assignment[literal]

def satisfies(assignment):
    return all(any(literal_true(lit, assignment) for lit in clause)
               for clause in CLAUSES.values())

def main():
    models = [dict(zip(VARS, bits)) for bits in product((False, True), repeat=len(VARS))
              if satisfies(dict(zip(VARS, bits)))]
    assert models, 'KB is inconsistent'
    assert all(m['O'] for m in models)
    assert all(not m['S'] for m in models)
    assert all(not m['F'] for m in models)
    assert any(m['L'] for m in models)
    assert any(not m['L'] for m in models)
    print(f'PASS: {len(models)} satisfying models')
    print('PASS: Omar guilty; Sara innocent; door not forced')
    print('PASS: Lina is undecidable from these clues')

if __name__ == '__main__':
    main()
