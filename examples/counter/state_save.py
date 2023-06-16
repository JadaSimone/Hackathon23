def save(i):
    with open("state.txt", "w") as file:
        file.write(str(i))
