import socket
import time
import os
import subprocess

#benchmark test for network bandwidth 
#send data packet, receive data packet, measure time to send and receive, calculate bandwidth of time and data size 

#set ip address and port
host = '10.0.2.15'
port = 80
#set data size
data_size = 1024 * 1024 * 10  

#create socket object and connect to host
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
except socket.error as err:
    print(f"{err}")
    exit()

loop = 50
bw = []

for i in range(loop):
    #time to send/receive data  
    start_time = time.time()
    s.sendall(b'0' * data_size)
    s.recv(data_size)
    end_time = time.time()

    #calculate bandwidth in mbps
    active = end_time - start_time
    bandwidth = data_size * 8 / (active * 1000000)
    bw.append(bandwidth)

avg_bw = sum(bw) / len(bw)
print(f"{avg_bw:.1f} mbps")

#close socket 
s.close()
