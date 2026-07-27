class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Animal makes a sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Rex")
print(dog.name,dog.make_sound())

cat = Cat("Tom")
print(cat.name,cat.make_sound())

class Fish(Animal):
    pass
fish = Fish("Goldfish")
print(fish.name,fish.make_sound())