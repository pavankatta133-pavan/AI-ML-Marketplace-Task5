import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_ZIP = os.path.join(ROOT, 'AI_ML_MARKETPLACE_TASK4.zip')
EXCLUDE_DIRS = {'myenv', '.venv', '__pycache__'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

with zipfile.ZipFile(OUT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Normalize path parts to check exclusions
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == '.':
            rel_parts = []
        else:
            rel_parts = rel_dir.split(os.sep)
        if any(part in EXCLUDE_DIRS for part in rel_parts):
            continue
        for fname in filenames:
            if fname == os.path.basename(OUT_ZIP):
                continue
            full = os.path.join(dirpath, fname)
            try:
                size = os.path.getsize(full)
            except OSError:
                continue
            if size > MAX_FILE_SIZE:
                continue
            arcname = os.path.relpath(full, ROOT)
            z.write(full, arcname)

print('WROTE', OUT_ZIP)
print('SIZE_BYTES', os.path.getsize(OUT_ZIP))
