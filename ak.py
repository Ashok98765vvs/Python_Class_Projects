class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print(f"{self.name} says Meow!")

    def nap(self, hours):
        print(f"{self.name} is coding for {hours} hours...")



milo = Cat("Milo", "Orange", 4)
milo.meow()
milo.nap(3)


ninja = Cat("Whisker", "Black", 2)
ninja.meow()
ninja.nap(5)