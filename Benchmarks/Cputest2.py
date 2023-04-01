import psutil
import sys

# Define the initial value of mem_usage_before_array
mem_usage_before_array = 0

while True:
    # Take the size of the array as input from the user
    size = int(input("Enter the size of the array: "))

    # Print the current CPU and memory usage
    print("Current CPU usage:", psutil.cpu_percent())
    print("Current memory usage:", psutil.virtual_memory().percent)

    # Create an array of the specified size to increase memory utilization
    array = [0] * size
    array_size = sys.getsizeof(array)

    # Print the final CPU and memory usage
    print("Final CPU usage:", psutil.cpu_percent())

    # Print the increase in memory usage
    current_mem_usage = psutil.virtual_memory().percent
    mem_increase = current_mem_usage - mem_usage_before_array
    print(f"Memory usage before array creation: {mem_usage_before_array}%")
    print(f"Memory usage after array creation: {current_mem_usage}%")
    print(f"Increase in memory usage: {mem_increase}%")
    
    # Update the memory usage before creating the array
    mem_usage_before_array = current_mem_usage
