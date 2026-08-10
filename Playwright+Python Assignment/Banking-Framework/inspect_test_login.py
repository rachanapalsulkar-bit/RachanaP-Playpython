from pathlib import Path
p = Path('tests/test_login.py')
for i, line in enumerate(p.read_text().splitlines(), 1):
    print(f'{i}: {line!r}')
