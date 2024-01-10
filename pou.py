import random

def minmax(value):
    if value < 0:
        return 0
    elif value > 100:
        return 100
    else:
        return value

class Pou:
    # inciciar
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = random.randint(0,50)
        self.energy = random.randint(50,100)
        self.happiness = random.randint(50,100)
        self.health = 100
        self.alive = True
        self.sleep_count = 0

    def status(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)
        print("Health:", self.health)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}"

    def play(self):
        self.hunger = minmax(self.hunger + random.randint(5, 10))
        self.energy = minmax(self.energy - random.randint(20, 30))
        self.happiness = minmax(self.happiness + random.randint(5, 10))
        self.health = minmax(self.health - random.randint(50, 60))
        self.check_health()

    def eat(self):
        self.hunger = minmax(self.hunger - random.randint(5, 10))
        self.energy = minmax(self.energy + random.randint(20, 20))
        self.happiness = minmax(self.happiness + random.randint(5, 10))
        self.health = minmax(self.health + random.randint(0, 5))
        self.check_health()

    def sleep(self):
        self.hunger = minmax(self.hunger + random.randint(5, 10))
        self.energy = minmax(self.energy + random.randint(30, 60))
        self.happiness = minmax(self.happiness + random.randint(0, 3))
        self.health = minmax(self.health + random.randint(0, 5))
        self.sleep_count += 1
        self.check_health()
    
    def pass_time(self):
        if self.sleep_count == 7:
            self.age += 1
            self.sleep_count = 0

    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} has died. Game over.")
            self.alive = False

toto = Pou("Toto")

while True:
    toto.status()
    option = input("What do you want to do? (play, eat, sleep, exit): ")

    if option == "play":
        toto.play()
    elif option == "eat":
        toto.eat()
    elif option == "sleep":
        toto.sleep()
    else:
        break
    toto.pass_time()
    print("A day has passed.\n")
