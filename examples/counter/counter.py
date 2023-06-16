import time
import sys

def count_values(startVal=0, maxVal=10, sleepTimer=1):
    for i in range(startVal, maxVal):
        print(i)
        file = open("../spot_state.txt", "w")
        file.write(str(i))
        file.close()
        time.sleep(sleepTimer)

if __name__ == '__main__':
    args = [int(arg) for arg in sys.argv[1:]]
    count_values(*args)
