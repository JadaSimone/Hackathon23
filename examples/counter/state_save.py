def save(i):
    with open("../spot_state.txt", "w") as file:
        file.write(str(i))
