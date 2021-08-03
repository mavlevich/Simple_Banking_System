# our class Ship
class Ship:
    def __init__(self, name, capacity, country):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.country = country

    # the old sail method that you need to rewrite
    def sail(self):
        print(f"The {self.name} has sailed for {self.country}!")


country = input()
black_pearl = Ship("Black Pearl", 800, country)
black_pearl.sail()
