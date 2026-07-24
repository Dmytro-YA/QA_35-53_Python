from pathlib import *

date_folder = Path('data')

file_path = date_folder / 'users.csv'
print(file_path)

print(file_path.exists())

screenshots_foldeer = Path('screenshots')
screenshots_foldeer.mkdir(exist_ok=True)
reports_folder = Path('reports/2026')
reports_folder.mkdir(parents=True)

