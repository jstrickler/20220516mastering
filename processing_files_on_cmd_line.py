import sys

for file_path in sys.argv[1:]: # skip sys.argv[0] AKA script name
    print(f"Processing {file_path}")
