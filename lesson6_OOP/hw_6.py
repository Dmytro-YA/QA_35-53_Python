#1
class Employee:
    def __init__(self, name,position,  salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}"

e1 = Employee("John", "Manager", 50000)
print(e1.get_info())

#2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def buy(self, amount):

        if self.quantity - amount < 0:
            return "Not enough products in stock"
        else:
            self.quantity -= amount
            return f"Left {self.quantity} {self.name} for price {self.price}$"

p = Product("Apple", 10, 100)
print(p.buy(55))
print(p.buy(45))
print(p.buy(1))

#3

class Vehicle:
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is moving"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"

#4
class User:
    country = "Israel"
    def __init__(self, name, age):
        self.name = name
        self.age = age

u1 = User("John", 25)
u2 = User("Jane", 30)
u3 = User("Bob", 20)
print(u1.country)
print(u2.country)
print(u3.country)
User.country = "Canada"
print(u1.country)
print(u2.country)
print(u3.country)

class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value
    def decrement(self):
        self.value -= 1
        return self.value
    def show(self):
        return self.value




