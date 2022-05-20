import os   # includes os.path
from datetime import datetime

folder = "DATA"
file_name = "alice.txt"

# file_path = f"{folder}/{file_name}"
file_path = os.path.join(folder, file_name)
print("file_path: {}\n".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))

raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}".format(raw_timestamp))

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp: {}".format(timestamp))

base_name = os.path.basename(file_path)
print("base_name: {}".format(base_name))

dir_name = os.path.dirname(file_path)
print("dir_name: {}".format(dir_name))

abs_path = os.path.abspath(file_path)
print("abs_path: {}".format(abs_path))

print("os.path.isdir(file_path): {}".format(os.path.isdir(file_path)))
print("os.path.isfile(file_path): {}".format(os.path.isfile(file_path)))

print("os.path.split(file_path): {}".format(os.path.split(file_path)))
print("os.path.splitext(file_path): {}".format(os.path.splitext(file_path)))


print("os.path.exists(file_path): {}".format(os.path.exists(file_path)))
missing_path = "DATA/wombats.txt"
print("os.path.exists(missing_path): {}".format(os.path.exists(missing_path)))

file_data = os.stat(file_path)
print("file_data: {}".format(file_data))

