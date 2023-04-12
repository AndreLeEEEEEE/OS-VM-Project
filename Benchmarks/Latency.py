# Author: Andre Le
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: Latency
# Purpose: Print the latency time for adjustable CPU and memory usage.

import os
from Uptime import getUptime

def main():
    toggle_uptime = input("Record uptime? (y/n) ").lower()
    if toggle_uptime == 'y':
        print("Uptime will be recorded\n")
    elif toggle_uptime == 'n':
        print("Uptime will not be recorded\n")
    else:
        print("Error: Invalid choice, ending program\n")
        return

    print("0 for CPU\n1 for Memory")
    test_mode = int(input("Select the test mode: "))

    terminal_command = ""
    # CPU
    if test_mode == 0:
        terminal_command = "sysbench --test=cpu"

        # cpu options
        # --cpu-max-prime = N, upper limit for primes generator [10000]

        num_prime = int(input("Enter an integer for the upper limit for primes generator: "))

        if num_prime <= 0:
            print("The number of primes cannot be negative or zero\n")
            return
        
        terminal_command += f" --cpu-max-prime={num_prime}"
    # Memory
    elif test_mode == 1:
        terminal_command = "sysbench --test=memory"

        # memory options
        # --memory-block-size, size of memory block for test [1K MB/1024 minimum]
        # --memory-total-size, total size of data to transfer [100 GB minimum]

        block_size = int(input("Enter an integer for memory block size (MB): "))
        total_size = int(input("Enter an integer for the total size of data to transfer (GB): "))

        if block_size > (total_size * 1024):
            print("Error: Block size cannot be larger than total size, ending program\n")
            return
        if block_size <= 0 or total_size <= 0:
            print("Error: Total size cannot be negative or zero, ending program\n")
            return
        if block_size < 1024:
            print("Error: Block size cannot be less than 1024 MB\n")
            return
        if total_size < 100:
            print("Error: Total size cannot be less than 100 GB\n")
        
        terminal_command += f" --memory-block-size={block_size}M"
        terminal_command += f" --memory-total-size={total_size}G"
    else:
        print("Error: No valid mode selected\n")
        return
    
    terminal_command += " run"

    if toggle_uptime == 'y':
        @getUptime
        def run_operation(command):
            os.system(command)
            return
        
        run_operation(terminal_command)
    else:
        os.system(terminal_command)

    return

if __name__ == "__main__":
    main()
