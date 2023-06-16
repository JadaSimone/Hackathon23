import time
import sys
import state_save

def count_values(startVal=0, maxVal=10000, sleepTimer=1):
    for i in range(startVal, maxVal):
        print(i)
        state_save.save(i)
        time.sleep(sleepTimer)

if __name__ == '__main__':
    args = [int(arg) for arg in sys.argv[1:]]
    count_values(*args)
