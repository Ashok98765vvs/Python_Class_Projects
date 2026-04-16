# 2_inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof! 🐶")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow! 🐱")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} says: Tweet! 🐦")

    def fly(self):
        print(f"{self.name} is flying!")


# Test
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

dog.speak()
cat.speak()
bird.speak()
bird.fly()
dog.eat()