class Pet:
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


def main():
    name = input("Name your pet")
    pet = Pet(name)

    while True:
        print("/nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check Status")
        print("5. Quit")

        choice = input("> ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.status()
        elif choice == "5":
            pet.status()
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid choice. Try again")

        pet.time_passes()


def status(self):
    print(f"\n(self.name)'s Status:")
    print(f"Hunger: {self.hunger}")
    print(f"Energy: {self.enery}")
    print(f"Happiness: {self.happiness}")


def time_passes(self):
    self.hunger = min(self.hunger + 5, 100)
    self.energy = max(self.energy - 5, 0)
    self.happiness = max(self.happiness - 5, 0)

    if self.hunger >= 100 or self.energy <= 0 or self.happiness <= 0:
        print(f"\nOh no! {self.name}'s needs weren't met.")
        print("Game Over!")
        exit()
