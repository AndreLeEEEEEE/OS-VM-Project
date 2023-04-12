import socket
import time
import os
import subprocess

#gets ip address of VM
def get_vm_ip():
    ip_command = "ip route get 1 | awk '{print $NF;exit}'"
    result = subprocess.check_output(ip_command, shell=True).decode('utf-8').strip()
    return result

#benchmark test for network bandwidth 
#send data packet, receive data packet, measure time to send and receive, calculate bandwidth of time and data size 

#set ip address and port
host = get_vm_ip()
port = 80

#set data size
data_size = 1024 * 1024 * 10  

#create socket object and connect to host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#time to send/receive data  
start_time = time.time()
s.sendall(b'0' * data_size)
s.recv(data_size)
end_time = time.time()

#calculate bandwidth in mbps
active = end_time - start_time
bandwidth = data_size * 8 / (active * 1000000)
print(f"{bandwidth:.1f} mbps")

#close socket 
s.close()