def get_state():
    file = open("state.txt", "r")
    current_state = file.read()
    return current_state

if __name__ == "__main__":
    current_state = get_state()
    print(current_state)
