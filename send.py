#!/usr/bin/env python3

import socket

HOST = '192.168.0.235'  # Standard loopback interface address (localhost)
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
                if count >= 5:
                    data = "END"
                    data = data.encode("utf-8")
                    # send data to client
                    conn.sendall(data)
                else:
                    data = "PC,1,2,3"
                    data = data.encode("utf-8")
                    # send data to client
                    conn.sendall(data)
                count = count + 1
            # client wil send close message then close
            if not data:
                break