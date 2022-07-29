import os
import shutil


# List created with all files in tmp
user_path = os.listdir("/var/tmp/")


# initialize dict
my_file_dict = {}


# Use function to create dictionary with each file as value of key
def create_file_dict():
    for i in range(len(user_path)):
        my_file_dict[i] = user_path[i]


create_file_dict()

for key, value in my_file_dict.items():
    if value.startswith('sysdiagnose'):
        shutil.rmtree(value)






