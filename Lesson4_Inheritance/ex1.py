#用DOG繼承ANIMAL

class Animal:
    def __init__(self):
        self.feet_number=4

    def shout(self):
        print("Hello! I'm an animal")

class Dog(Animal):
    pass

puppy=Dog()
puppy.shout()
