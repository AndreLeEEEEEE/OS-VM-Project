# Author: Andre Le
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: Latency
# Purpose: 

import os
# import argparse
from Uptime import getUptime

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-t", "--TestMode", type=int)

    # args = parser.parse_args()
    # test_mode = args.TestMode 

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

        num_prime = int(input("Enter an integer for the number of prime numbers to be generated: "))

        if num_prime <= 0:
            print("The number of primes cannot be negative or zero\n")
            return
        
        terminal_command += f" --cpu-max-prime={num_prime}"
    # Memory
    elif test_mode == 1:
        terminal_command = "sysbench --test=memory"

        # memory options
        # --memory-block-size, size of memory block for test [1K MB]
        # --memory-total-size, total size of data to transfer [100 GB]

        block_size = int(input("Enter an integer for memory block size (MB): "))
        total_size = int(input("Enter an integer for the total size of data to transfer (GB): "))

        if block_size > (total_size * 1024):
            print("Error: Block size cannot be larger than total size, ending program\n")
            return
        if block_size <= 0 or total_size <= 0:
            print("Size cannot be negative or zero, ending program\n")
            return
        
        terminal_command += f" --memory-block-size={block_size}M"
        terminal_command += f" --memory-total-size={total_size}G"
    # I/O
    # elfi test_mode == 2:
    #   pass
    else:
        print("Error: No valid mode selected\n")
        return
    

    terminal_command += " run"

    if toggle_uptime == 'y':
        system_call = getUptime(os.system(terminal_command))
        system_call()
    else:
        os.system(terminal_command)

    return

if __name__ == "__main__":
    main()
