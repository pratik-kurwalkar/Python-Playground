# File Handling

from pathlib import Path

path1 = Path()  # Denotes current path
for file in path1.glob('*.py'):
    print(file)

path2 = Path("testDirectory")
path2.rmdir() if path2.exists() else None
# path2.mkdir()
