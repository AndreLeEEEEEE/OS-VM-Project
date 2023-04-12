# Author: Sai Anurag Doddi 
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: CPU and Memory Utilization
# Purpose: Monitor CPU and memory usage after creating an array.
# Update - Added uptime functionality is untested

import psutil
import sys
from Uptime import getUptime

def make_array(size: int, mem_usage_before_array: float):
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent()

    # Print the current CPU and memory usage
    mem_usage = psutil.virtual_memory()
    print(f"Current CPU usage: {cpu_percent}%")
    print(f"Current memory usage: {mem_usage.used/1024/1024:.2f} MB/{mem_usage.total/1024/1024:.2f} MB ({mem_usage.percent}%)")

    # Create an array of the specified size to increase memory utilization
    # Purposely not accessed 
    array = [0] * size
    # array_size = sys.getsizeof(array)

    # Print the increase in memory usage
    current_mem_usage = mem_usage.percent
    mem_increase = current_mem_usage - mem_usage_before_array
    cpu_percent_final = psutil.cpu_percent()
    cpu_percent_change = cpu_percent_final - cpu_percent
    
    print(f"Final CPU usage: {cpu_percent_final}%")
    print(f"Memory usage before array creation: {mem_usage_before_array}%")
    print(f"Memory usage after array creation: {current_mem_usage}%")
    print(f"Increase in memory usage: {mem_increase}%")
    print(f"Change in CPU usage: {cpu_percent_change}%")
    
    # Update the memory usage before creating the array
    return current_mem_usage

def main():
    toggle_uptime = input("Record uptime? (y/n) ").lower()
    if toggle_uptime == 'y':
        print("Uptime will be recorded\n")
    elif toggle_uptime == 'n':
        print("Uptime will not be recorded\n")
    else:
        print("Error: Invalid choice, ending program\n")
        return

    # Define the initial value of mem_usage_before_array
    mem_usage_before_array = psutil.virtual_memory().percent

    while True:
        # Take the size of the array as input from the user
        size = int(input("Enter the size/length of the array: "))
        if toggle_uptime == 'y':
            @getUptime
            def run_operation():
                mem_usage_before_array = make_array(size, mem_usage_before_array)
                return
            
            run_operation()
        else:
            mem_usage_before_array = make_array(size, mem_usage_before_array)

if __name__ == "__main__":
    main()
