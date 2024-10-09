# Classes

# Classes create objects

class Mammal:
    def __init__(self, fur_color, diet):
        self.fur_color = fur_color
        self.diet = diet
        self.warm_blooded = True

    def breath(self):
        print("inhale")
        print("exhale")


# Dog will inherit from Mammal
class Dog(Mammal):
    def __init__(self, fur_color, diet, name):
        super().__init__(fur_color, diet)
        self.name = name

    # method override 
    def breath(self):
        print("pant\npant\npant")

my_dog = Dog("black", "dog food", "Fido")
print("------Fido the dog -------")
print(my_dog.fur_color)
print(my_dog.diet)
print(my_dog.name)
my_dog.breath()
        
genenric_mammal = Mammal("gray", "donuts")
print("------generic mammal -------")
print(genenric_mammal.fur_color)
print(genenric_mammal.diet)
#print(genenric_mammal.name) Mammal class doesn't have a name

genenric_mammal.breath()