def get_state():
    file = open("../spot_state.txt", "r")
    current_state = file.read()
    return current_state

current_state = get_state()
print(current_state)