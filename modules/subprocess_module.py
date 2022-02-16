"""
Python subprocess module
 - Used to execute Operating System commands
 - Intends to replace several older modules and functions (os.system && os.spawn)
 - Avoid shell=True (Forks a new shell)
""" 

import subprocess

command = ["ls", "-l"]

sp = subprocess.Popen(
        command, 
        shell=False, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

rt = sp.wait() # 0 or non-zero 

output, error = sp.communicate()

print(output)