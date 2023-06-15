import time

def count_values (startVal=0, maxVal=10, sleepTimer=1):
    for i in range(startVal, maxVal):
        print(i)
        file = open("../spot_state.txt", "w")
        file.write(str(i))
        file.close()
        time.sleep(sleepTimer)

count_values(3, 10, 1)
file = open("../spot_state.txt", "r")
print()
print(file.read())
