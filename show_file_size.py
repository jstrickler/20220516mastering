import sys
import os

file_paths = sys.argv[1:]  # start with 2nd element of argv

for file_path in file_paths:
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"{file_size:10d} {file_path}")
    else:
        print(f"{file_path} is not a file!", file=sys.stderr)

