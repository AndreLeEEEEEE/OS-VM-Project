# Author: Andre Le
# CSCI 5573 - Operating Systems
# Final Project Benchmark
# Criterion: Uptime
# Purpose: Monitor the how long a system stays up as it runs an intensive process. 
# This benchmark provide a decorator/wrapper and needs to be run with another benchmark.

import time
import os
import argparse
import math
from Latency import main as latency

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

        return process_name, uptime, process_output
    return timer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--benchmark", type=int)

    args = parser.parse_args()
    benchmark_name = args.benchmark
    decoratedFunction = None

    if benchmark_name == "CPUUtilization":
        # Waiting for creation
        pass
    elif benchmark_name == "MemoryUsage":
        # Waiting for creation
        pass
    elif benchmark_name == "DiskIO":
        # Waiting for creation
        pass
    elif benchmark_name == "NetworkBandwidth":
        # Waiting for creation
        pass
    elif benchmark_name == "Latency":
        # Come back and add passed arguments once Latency is complete
        decoratedFunction = getUptime(latency)
    else:
        print("A valid name was not passed, ending benchmark.")
        return

    p_name, uptime, p_output = decoratedFunction()

    print(f"System (Linux OS) uptime: {os.system('uptime -p')}\n")

    print(f"Process: {p_name}\n")

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

    print(f"Process output:\n{p_output}\n")

    return

if __name__ == "__main__":
    main()
