class Dog:
    species = 'Cans familiars'

    def __init__(self, name):
        self.name = name

dog1 = Dog("Rex")
dog2 = Dog("Max")
print(dog1.name,"-", dog1.species,"\n",dog2.name," - ", dog2.species)

Dog.species = "Canis lupus familiars"
print(dog1.species, dog1.name)
print(dog2.species, dog2.name)