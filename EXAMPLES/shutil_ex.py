#!/usr/bin/env python
#
import shutil
import os

shutil.copy('../DATA/alice.txt', 'betsy.txt') # <1>
# cp A B  Mac/Linux
# copy A B Win
# os.system(f"cp {src_name} {destination_name}")

print("betsy.txt exists:", os.path.exists('betsy.txt'))

shutil.move('betsy.txt', 'fred.txt') # <2>
# mv A B Mac/Linux
# move A B Win
print("betsy.txt exists:", os.path.exists('betsy.txt'))
print("fred.txt exists:", os.path.exists('fred.txt'))

new_folder = 'remove_me'

os.mkdir(new_folder) # <3>
shutil.move('fred.txt', new_folder)

archive_name = new_folder
folder_to_zip = new_folder

shutil.make_archive(archive_name, 'zip', folder_to_zip) # <4>
shutil.make_archive(archive_name, 'tar', folder_to_zip) # <4>
shutil.make_archive(archive_name, 'gztar', folder_to_zip) # <4>
shutil.make_archive(archive_name, 'bztar', folder_to_zip) # <4>

print("{}.zip exists:".format(new_folder), os.path.exists(new_folder + '.zip'))

print("{} exists:".format(new_folder), os.path.exists(new_folder))

shutil.rmtree(new_folder) # <5>

print("{} exists:".format(new_folder), os.path.exists(new_folder))

