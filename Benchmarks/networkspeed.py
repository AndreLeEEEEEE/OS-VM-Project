import sys
import speedtest
from Uptime import getUptime

def networkspeed(tests):
    #create empty arrays for speed values
    dl = []
    ul = []
    #run speedtest number of runs
    for test in range(tests):
        #speed test function
        s = speedtest.Speedtest()
        #get best server for speed test
        s.get_best_server()

        #get download speed
        dl_speed = s.download()
        #get upload speed
        ul_speed = s.upload()
        #convert download speed from bits to mbps
        dl_speed = dl_speed / 1000000
        #convert upload speed from bits to mbps
        ul_speed = ul_speed / 1000000
        #add download speed to array 
        dl.append(dl_speed)
        #add upload speed to array
        ul.append(ul_speed)
    #calculate average download speed
    dl_speed_avg = sum(dl) / len(dl)
    #calculate average upload speed
    ul_speed_avg = sum(ul) / len(ul)
    #print download/upload
    print("download speed mbps: " + str(dl_speed_avg))
    print("upload speed mbps: " + str(ul_speed_avg))

def main():
    toggle_uptime = input("Record uptime? (y/n) ").lower()
    if toggle_uptime == 'y':
        print("Uptime will be recorded\n")
    elif toggle_uptime == 'n':
        print("Uptime will not be recorded\n")
    else:
        print("Error: Invalid choice, ending program\n")
        return
    
    #number of tests
    num_tests = int(input("Enter the number of tests: "))

    if toggle_uptime == 'y':
        @getUptime
        def run_operation():
            networkspeed(num_tests)
            return
        
        run_operation()
    else:
        networkspeed(num_tests)

    return

if __name__ == "__main__":
    main()
