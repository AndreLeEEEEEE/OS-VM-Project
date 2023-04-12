# Author: Kyu Ro
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: Disk I/O
# Purpose: Monitor disk I/O.
# Update - Added uptime functionality and adjustable integer functionality are untested

import os
import time
from Uptime import getUptime

def diskio(num_iterations: int):
    #benchmark test for disc i/o
    #create file of specific size, measure read/write time of file 100 times

    #size of file
    file_size = 1024 * 1024 * 10 

    #make file 
    with open("test.bin", "wb") as f:
        f.write(os.urandom(file_size))

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

def main():
    toggle_uptime = input("Record uptime? (y/n) ").lower()
    if toggle_uptime == 'y':
        print("Uptime will be recorded\n")
    elif toggle_uptime == 'n':
        print("Uptime will not be recorded\n")
    else:
        print("Error: Invalid choice, ending program\n")
        return
    
    #number of runs
    num_iterations = int(input("Enter the number of iterations: "))
    
    if toggle_uptime == 'y':
        @getUptime
        def run_operation():
            diskio(num_iterations)
            return
        
        run_operation()
    else:
        diskio(num_iterations)

    return

if __name__ == "__main__":
    main()
