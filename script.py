import os
import re

def find_sysdiag():
    pattern = "sysdiagnose_[\d]"
    user_path = os.listdir("/var/tmp/")
    for file in user_path:
        if (re.search(pattern[pattern])) in file:
            print(file)


find_sysdiag()



