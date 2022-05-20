import os

start_dir = "."

skip = ".git"
for curr_dir, sub_dirs, files in os.walk(start_dir):
    if skip in sub_dirs:
        sub_dirs.remove(skip)
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"   {file_size:8d} {file_name}")
            # print("    {:8d} {}".format(file_size, file_name))


