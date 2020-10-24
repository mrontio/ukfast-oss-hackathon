# We want to create a script to find lab resources and be able to find where they are in the lab enviroment.
# A bit like an iDRAC opensource

import os
import socket
print("hello")


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(ip)
