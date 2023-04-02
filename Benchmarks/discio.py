import os
import time

#benchmark test for disc i/o
#create file of specific size, measure read/write time of file 100 times

#size of file
file_size = 1024 * 1024 * 10 

#make file 
with open("test.bin", "wb") as f:
    f.write(os.urandom(file_size))

#number of runs
num_iterations = 100

#time to read file 
start_time = time.time()
for i in range(num_iterations):
    with open("test.bin", "rb") as file:
        file.read()
end_time = time.time()
read_time = end_time - start_time
print(f"{num_iterations} * {read_time:.1f} seconds")

#time to write file 
start_time = time.time()
for i in range(num_iterations):
    with open("test.bin", "wb") as file:
        file.write(os.urandom(file_size))
end_time = time.time()
write_time = end_time - start_time
print(f"{num_iterations} * {write_time:.1f} seconds")

