import random

def minmax(value):
    if value < 0:
        return 0
    elif value > 100:
        return 100
    else:
        return value

def status(state):
    print("Name:", state["name"])
    print("Age:", state["age"])
    print("Hunger:", state["hunger"])
    print("Energy:", state["energy"])
    print("Happiness:", state["happiness"])
    print("Health:", state["health"])

def play(state):
    new_state = dict(state)
    new_state["hunger"] = minmax(state["hunger"] + random.randint(5, 10))
    new_state["energy"] = minmax(state["energy"] - random.randint(20, 30))
    new_state["happiness"] = minmax(state["happiness"] + random.randint(5, 10))
    new_state["health"] = minmax(state["health"] - random.randint(50, 60))
    check_health(new_state)
    return new_state

def eat(state):
    new_state = dict(state)
    new_state["hunger"] = minmax(state["hunger"] - random.randint(5, 10))
    new_state["energy"] = minmax(state["energy"] + random.randint(20, 20))
    new_state["happiness"] = minmax(state["happiness"] + random.randint(5, 10))
    new_state["health"] = minmax(state["health"] + random.randint(0, 5))
    check_health(new_state)
    return new_state

def sleep(state):
    new_state = dict(state)
    new_state["hunger"] = minmax(state["hunger"] + random.randint(5, 10))
    new_state["energy"] = minmax(state["energy"] + random.randint(30, 60))
    new_state["happiness"] = minmax(state["happiness"] + random.randint(0, 3))
    new_state["health"] = minmax(state["health"] + random.randint(0, 5))
    new_state["sleep_count"] += 1
    check_health(new_state)
    return new_state

def pass_time(state):
    new_state = dict(state)
    if new_state["sleep_count"] == 7:
        new_state["age"] = str(int(new_state["age"]) + 1)
        new_state["sleep_count"] = 0
    check_health(new_state)
    return new_state

def check_health(state):
    if state["health"] <= 0:
        print(f"{state['name']} has died. Game over.")
        state["alive"] = False

state = {
    "name": "TOTO",
    "age": "0",
    "hunger": random.randint(0, 50),
    "energy": random.randint(50, 100),
    "happiness": random.randint(50, 100),
    "health": 100,
    "alive": True,
    "sleep_count": 0
}

while state["alive"]:
    status(state)
    option = input("What do you want to do? (play, eat, sleep, exit): ")

    if option == "play":
        state = play(state)
    elif option == "eat":
        state = eat(state)
    elif option == "sleep":
        state = sleep(state)
    else:
        break
    state = pass_time(state)
    print("A day has passed.\n")