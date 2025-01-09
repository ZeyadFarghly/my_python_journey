class Dog:
    def __init__(self):
        self.temperament = "loyal"

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"
dog = Dog()
sparky = Labrador()
print(f"a dog is {dog.temperament}")
print(f"sparky is {sparky.temperament}")