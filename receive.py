#!/usr/bin/env python3
import socket
import subprocess


# example for using function below
# data = 'PC,R,1,-2,O,2,3,4,5,6,7,C,11,23,P,2,3,4,5,6,7,8,9,12,13,E'
# data = data.split(',')
# data = data_spliting(data)
# pocess data from PC and output standard output to send to stm
def data_spliting(data):
    R = []
    O = []
    C = []
    P = []
    capture_flag = 0
    for i in range(len(data)):
        if data[i] == 'R':
            capture_flag = 1
            continue
        elif data[i] == 'O':
            capture_flag = 2
            continue
        elif data[i] == 'C':
            capture_flag = 3
            continue
        elif data[i] == 'P':
            capture_flag = 4
            continue
        elif data[i] == 'E':
            continue

        if capture_flag == 1:
            R.append(data[i])
        elif capture_flag == 2:
            O.append(data[i])
        elif capture_flag == 3:
            C.append(data[i])
        elif capture_flag == 4:
            P.append(data[i])

    print(R, '\n', O, '\n', C, '\n', P)
    return (R, O, C, P)


# process data from standard output and send separately into STM
# data 0 1 2 3 = Robot Obstacle CameraPose Path
def send_to_dk2(data):
    for i in range(len(data)):
        if len(data[i]) > 1:
            send_str = "----"
            if i == 0:  # Robot
                send_str = send_str + "R,"
                send_str = send_str + str(data[i][0]) + "," + str(data[i][1]) + ","
            elif i == 1:  # Obs
                send_str = send_str + "O,"
                for j in range(int(len(data[i])/2)):
                    send_str = send_str + str(data[i][j*2]) + "," + str(data[i][j*2 + 1]) + ","
            elif i == 2:  # Campos
                send_str = send_str + "C,"
                send_str = send_str + str(data[i][0]) + "," + str(data[i][1]) + ","
            elif i == 3:  # Path
                send_str = send_str + "P,"
                for j in range(int(len(data[i])/2)):
                    send_str = send_str + str(data[i][j*2]) + "," + str(data[i][j*2 + 1]) + ","
            send_str = send_str.rstrip(',')
            send_str = send_str + "--"
            f = open("/dev/ttyRPMSG0", "w")
            result = subprocess.run(['echo', send_str], stdout=f)
            print(result.stdout)
            print(send_str)

# command list
cmd1 = ['cat', '/sys/class/remoteproc/remoteproc0/state']
cmd2 = ['sh', '/usr/local/projects/Walle_CM4/fw_cortex_m4.sh start']
cmd3 = ['echo', 'start']
cmd4 = ['echo', 'stop']

# check state of CM4
print("checking state of core M4: ")
result = subprocess.run(cmd1, stdout=subprocess.PIPE)
result = result.stdout.decode("utf-8").rstrip()
print(result)

# start M4 core
if result == "offline":
    print('start core M4...')
    result = subprocess.run(cmd2, stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8").rstrip()
    print(result)

# start listening to PC
HOST = '192.168.43.77'  # The server's hostname or IP address
PORT = 11223  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # send DK2 as first connection word
    data = "DK2"
    data = data.encode("utf-8")
    s.sendall(data)
    while (1):
        data = s.recv(1024)
        data = data.decode("utf-8")
        if data.find('END') == 0:
            break
        elif data.find('PC') == 0:
            data2 = data.lstrip('PC,')
            print('receive from PC:', data2)

            # data process
            # send data to DK2
            data = data.split(',')
            data = data_spliting(data)
            send_to_dk2(data)

            # send again
            data = "DK2"
            data = data.encode("utf-8")
            s.sendall(data)

# closed Core M4
f = open("/sys/class/remoteproc/remoteproc0/state", "w")
result = subprocess.run(cmd4, stdout=f)

print('Received', repr(data))
