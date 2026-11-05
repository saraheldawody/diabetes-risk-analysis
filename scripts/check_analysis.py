"""Validate bundled data and smoke-run notebook code from the repository root."""
import csv
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SHA256 = 'b78029447fae2743b3218bb2b76ef0d04afe8d7e55ce2faf4d1ec82d8f8ae8ac'


def main():
    os.chdir(ROOT)
    assert hashlib.sha256(Path('diabetes.csv').read_bytes()).hexdigest() == EXPECTED_SHA256, 'Dataset changed; review checks and provenance'
    rows = list(csv.DictReader(Path('diabetes.csv').open()))
    expected = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    assert list(rows[0]) == expected, 'Unexpected schema'
    assert len(rows) == 768, 'Unexpected row count'
    assert all(r['Outcome'] in {'0', '1'} for r in rows), 'Invalid target'
    assert sum(r['Outcome'] == '1' for r in rows) == 268
    assert all(v and float(v) >= 0 for r in rows for v in r.values())
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    # Close figures as they are displayed to keep headless execution bounded.
    plt.show = lambda *args, **kwargs: plt.close('all')
    notebook = json.loads(Path('diabetes.ipynb').read_text())
    namespace = {'__name__': '__main__'}
    for index, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            exec(compile(''.join(cell['source']), f'diabetes.ipynb:cell-{index}', 'exec'), namespace)
    assert namespace['raw_data'].equals(namespace['pd'].read_csv('diabetes.csv'))
    print('PASS: data checks and all notebook code cells executed.')


if __name__ == '__main__':
    main()
