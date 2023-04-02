import psutil
import sys

# Define the initial value of mem_usage_before_array
mem_usage_before_array = 0

while True:
    # Take the size of the array as input from the user
    size = int(input("Enter the size of the array: "))

    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent()

    # Print the current CPU and memory usage
    mem_usage = psutil.virtual_memory()
    print(f"Current CPU usage: {cpu_percent}%")
    print(f"Current memory usage: {mem_usage.used/1024/1024:.2f} MB/{mem_usage.total/1024/1024:.2f} MB ({mem_usage.percent}%)")

    # Create an array of the specified size to increase memory utilization
    array = [0] * size
    array_size = sys.getsizeof(array)

    # Print the final CPU and memory usage
    print(f"Final CPU usage:{cpu_percent}%")

    # Print the increase in memory usage
    current_mem_usage = mem_usage.percent
    mem_increase = current_mem_usage - mem_usage_before_array
    print(f"Memory usage before array creation: {mem_usage_before_array}%")
    print(f"Memory usage after array creation: {current_mem_usage}%")
    print(f"Increase in memory usage: {mem_increase}%")
    
    # Update the memory usage before creating the array
    mem_usage_before_array = current_mem_usage
