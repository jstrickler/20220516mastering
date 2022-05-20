import os

all_files = os.listdir('DATA')
print("all_files: {}\n".format(all_files))
print('-' * 60)

all_files_gen = os.scandir('DATA')
print("all_files_gen: {}".format(all_files_gen))
for file_obj in all_files_gen:
    print(file_obj, file_obj.name, file_obj.is_dir())

