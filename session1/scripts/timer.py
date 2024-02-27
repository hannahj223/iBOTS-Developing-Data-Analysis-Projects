import time
import sys

time.sleep(1) # sleep for 1 second

your_time = int(sys.argv[1])


for i in range(your_time):
    print(i +1)
    time.sleep(1)
