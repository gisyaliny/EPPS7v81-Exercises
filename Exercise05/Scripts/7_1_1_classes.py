"""
Programming in Python for Social Science
Phillip Brooker

7. 1. 1. CLASSES
"""


# Below is how you create a class - there are lots of things going on, but we
# will explore these in more detail in the relevant section of the book. For now
# suffice to say that this class contains attributes and methods (i.e. functions
# that a zookeeper might find useful.

class Animal:
    animal_list = []
    animal_count = 0

    def __init__(self, name, gender, species, age):
        self.name = name
        self.gender = gender
        self.species = species
        self.age = age
        Animal.animal_list.append (self)
        Animal.animal_count = Animal.animal_count + 1

    def displayCount():
        print ("There are " + str (Animal.animal_count) + " animals in the zoo.")

    def displayAnimal(self):
        print (self.name + " is a " + self.gender + " " + self.species + ".")
        print (self.name + " is " + str (self.age) + " years old.")


# So the "blueprint" bit of the class is outlined above, but we need to fill it
# with entries - below is a list of animals in the zoo, and various properties
# of them. This is how you assign things to the class we've just built.

gill = Animal ("Gill", "female", "bison", 14)
bruce = Animal ("Bruce", "male", "zebra", 7)
tony = Animal ("Tony", "male", "orangutan", 22)
rebecca = Animal ("Rebecca", "female", "tree frog", 1)
sweaty = Animal ("Sweaty", "male", "fox", 34)
slippy = Animal ("Slippy", "female", "penguin", 4)

# Now try playing around with each animal's attributes - let's call up certain
# bits of information about the animals in the zoo. Type this into the shell:
tony.species
sweaty.age
slippy.gender

# Now try playing around with the class methods (i.e. functions) we built in.
# Start by typing the following function calls into the shell:
"""
Animal.displayCount()
Animal.displayAnimal(rebecca)
"""
