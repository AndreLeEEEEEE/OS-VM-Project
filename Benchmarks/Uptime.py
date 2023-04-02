# Author: Andre Le
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: Uptime
# Purpose: Monitor the how long a system stays up as it runs an intensive process. 
# This benchmark provide a decorator/wrapper and needs to be run with another benchmark.

import time
import os
import math

def getUptime(process):
    def timer(*args, **kwargs):
        print("Uptime monitor has been called\n")

        print("Start monitoring\n")
        start = time.time()

        process_output = process(*args, **kwargs)

        end = time.time()
        print("\nEnd of monitoring\n")

        process_name = process.__name__
        # uptime unit is seconds
        uptime = end - start
        if process_output is None:
            process_output = "The monitored process had no printed end output.\n"

        print(f"System (Linux OS) uptime: {os.system('uptime -p')}\n")

        print(f"Process: {process_name}\n")

        # Obtain hours
        hours = math.floor(uptime / 3600)
        # Obtain minutes
        uptime %= 3600
        minutes = math.floor(uptime / 60)
        # Obtain seconds
        seconds = int(uptime % 60)

        print(f"Process uptime:\n")
        print(f"Hours: {hours}\n")
        print(f"Minutes: {minutes}\n")
        print(f"Seconds: {seconds}\n\n")

        print(f"Process output:\n{process_output}\n")

        return
    return timer

def main():
    print("This benchmark is a decorator that can be run on top of another benchmark.\n")
    print("Therefore, this benchmark cannot be run by itself as there would be nothing to monitor.\n")
    return

if __name__ == "__main__":
    main()
