import socket
import time

#benchmark test for network bandwidth 
#send data packet, receive data packet, measure time to send and receive, calculate bandwidth of time and data size 

#set ip address and port
host = ''
port = 80

#set data size
data_size = 1024 * 1024 * 10  

#create socket object and connect to host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#time to send data  
start_time = time.time()
s.sendall(b'0' * data_size)
s.recv(data_size)
end_time = time.time()

#calculate bandwidth
active = end_time - start_time
bandwidth = data_size * 8 / (active * 1000000)
print(f"{bandwidth:.1f} mbps")

#close socket 
s.close()