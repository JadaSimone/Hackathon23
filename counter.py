import time

def count_values (maxVal, sleepTimer):
    for i in range(maxVal):
        print(i)
        file = open("../spot_state.txt", "w")
        file.write(str(i))
        file.close()
        time.sleep(sleepTimer)

count_values(10, 5)
file = open("../spot_state.txt", "r")
print()
print(file.read())