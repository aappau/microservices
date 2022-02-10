"""
Python OS module
 - Used to execute Operating System commands
 - os.system(): Does not store output of the commands
"""

"""
Managing files and directories 
 * os.chdir(<path>)
 * os.getcwd()
 * os.listdir(<path>)

 * os.mknod(<file_name>)
 * os.rename(<file_name>)

 * os.mkdir(<dir_name>)
 * os.rmdir(<dir_name>)

 * os.makedirs(<dir_name>/<dir_name>)
 * os.removedirs(<dir_name>/<dir_name>)   
"""

import os


os.system("clear")
os.system("pwd")
os.system("ls -l")


# environment variable
env_variables = os.environ
whoami = os.environ.get("USER")
print(whoami)


# os.path
print(os.path.exists("/etc/hosts"))
print(os.path.getsize("/etc"))

print(os.path.isfile("/etc/hosts"))
print(os.path.isdir("/etc/hosts"))
print(os.path.islink("/etc/hosts"))

print(os.path.basename('/etc/hosts'))
print(os.path.dirname('/etc/hosts'))
print(os.path.join("/home", "testfile"))
