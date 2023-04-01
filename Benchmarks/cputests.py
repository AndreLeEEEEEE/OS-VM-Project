import psutil
import time

data = []

while True:
    # Ask user for memory size in GB
    size = int(input("Enter memory size in GB: "))

    try:
        # Allocate memory
        data.append(bytearray(size * 1024 * 1024 * 1024))
    except MemoryError:
        print("Memory overloaded. Program crashed.")
        break

    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent()

    # Get memory usage
    mem = psutil.virtual_memory()
    mem_used_percent = mem.percent

    # Print CPU and memory usage
    print("CPU usage:", cpu_percent, "%")
    print("Memory usage:", mem_used_percent, "%")

    # Wait for 1 second
    time.sleep(1)