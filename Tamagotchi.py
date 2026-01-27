def __init__(self, name):
    self.name = name
    self.hunger = 50
    self.energy = 50
    self.happiness = 50


def feed(self):
    self.hunger = max(self.hunger - 20, 0)
    print(f"{self.name} has been fed!")


def play(self):
    if self.energy >= 20:
        self.happiness = min(self.happiness + 20, 100)
        self.energy -= 20
        print(f"{self.name} played and had fun!")
    else:
        print(f"{self.name} is too tired to play")


def sleep(self):
    self.energy = min(self.energy + 30, 100)
    self.hunger = min(self.hunger + 10, 100)
    print(f"{self.name} took a nap.")
