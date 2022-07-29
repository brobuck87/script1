import os


# List created with all files in tmp
import stat

user_path = os.listdir("/var/tmp/")

# initialize dict
my_file_dict = {}


# Use function to create dictionary with each file as value of key
def create_file_dict():
    for i in range(len(user_path)):
        my_file_dict[i] = user_path[i]


create_file_dict()

# for key, value in my_file_dict.items():
#     if value.startswith('sysdiagnose'):
#         os.chmod("/var/tmp/", stat.S_IWRITE)
#         os.remove("/var/tmp/" + value)






