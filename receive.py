#!/usr/bin/env python3

import socket
import os
# simple test only
# subprocess.run(["ls", "-l"])

# check state of CM4
print("checking state of cor M4:")
cmd = "cat /sys/class/remoteproc/remoteproc0/state"

stream = os.popen('echo Returned output')
output = stream.read()

print(returned_value)
cmd = "sh /usr/local/projects/Walle_CM4/fw_cortex_m4.sh start"
returned_value = os.system(cmd)  # returns the exit code in unix
print(returned_value)
#cmd = "echo start > /sys/class/remoteproc/remoteproc0/state"
#returned_value = os.system(cmd)  # returns the exit code in unix
#print(returned_value)
cmd = "cat /sys/class/remoteproc/remoteproc0/state"
returned_value = os.system(cmd)  # returns the exit code in unix
print(returned_value)
cmd = "echo stop > /sys/class/remoteproc/remoteproc0/state"
returned_value = os.system(cmd)  # returns the exit code in unix
print(returned_value)
cmd = "cat /sys/class/remoteproc/remoteproc0/state"
returned_value = os.system(cmd)  # returns the exit code in unix
print(returned_value)

#subprocess.run(["cat", "/sys/class/remoteproc/remoteproc0/state"])
#echo $(tr -d '\0' < /sys/c
# lass/remoteproc/remoteproc0/state)
#CMD12 = echo start > /sys/class/remoteproc/remoteproc0/state
#CMD13 = echo stop > / sys /class /remoteproc / remoteproc0 / state
#CMD17 = echo '----0,0,0--' > /dev/ttyRPMSG0
#CMD21 = sh /usr/local/projects/Walle_CM4/fw_cortex_m4.sh
#CMD22 = rm /lib/firmware/Walle_CM4.elf
#CMD23 = cp /usr/local/projects/Walle_CM4/lib/firmware/Walle_CM4.elf /li/firmware/
#CMD24 = cp /usr/local/projects/Walle_CM4/lib/firmware/Walle_CM4.elf /lib/firmware/Walle_CM4.elf
#CMD25 = sh /usr/local/projects/Walle_CM4/fw_cortex_m4.sh start

# HOST = '192.168.0.235'  # The server's hostname or IP address
# PORT = 11223        # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     data = "DK2"
#     data = data.encode("utf-8")
#     s.sendall(data)
#     while(1):
#         data = s.recv(1024)
#         data = data.decode("utf-8")
#         if data.find('END') == 0:
#             break
#         elif data.find('PC') == 0:
#             print('receive from PC:',data.lstrip('PC,'))
#             # subprocess.run(["ls", "-l"])
#             data = "DK2"
#             data = data.encode("utf-8")
#             s.sendall(data)
#
# print('Received', repr(data))
#
