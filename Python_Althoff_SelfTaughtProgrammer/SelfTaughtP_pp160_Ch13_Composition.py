
# Composition models the "has a" relationship by storing an object as a
# variable in another object. For example, you can use composition to model
# the relationship between a dog and its owner (the dog has an owner).

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

nick = Person("Nick Burkhardt")
monroe = Dog("Monroe", "Blutbad", nick)

print(monroe.owner.name)
