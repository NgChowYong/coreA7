#!/usr/bin/env python3

# turn into ros version

import socket

HOST = '192.168.43.77'  # Standard loopback interface address (localhost)
PORT = 11223        # Port to listen on (non-privileged ports are > 1023)

count = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # stream using TCP, afinet is using ipv4
    s.bind((HOST, PORT))
    # creating listening port
    s.listen()
    # accept from client request/connect
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # get data from client
            data = conn.recv(1024)
            data = data.decode("utf-8")
            print(data)
            if data.find('DK2') == 0:
                print('sending data : PC,1,2,3')
                if count >= 1:
                    data = "END"
                    data = data.encode("utf-8")
                    # send data to client
                    conn.sendall(data)
                else:
                    data = 'PC,R,1,-2,C,11,23,P,2,3,4,5,6,7,8,9,12,13,E'
                    data = data.encode("utf-8")
                    # send data to client
                    conn.sendall(data)
                count = count + 1
            # client wil send close message then close
            if not data:
                break
