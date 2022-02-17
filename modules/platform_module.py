"""
Python Platform module
 - Used to write cross platform scripts
"""

import platform


os = platform.system()
arch = platform.architecture()
mac = platform.machine()
release = platform.release()
py_version = platform.python_version()

print(os, arch, mac, release, py_version)