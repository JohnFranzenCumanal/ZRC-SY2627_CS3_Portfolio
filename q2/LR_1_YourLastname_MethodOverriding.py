
class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def eat(self):
        return "eats food"

    def make_sound(self):
        return "makes a sound"


class Lion(Animal):
    def make_sound(self):
        return "roars loudly!"

    def eat(self):
        return "eats fresh meat."


class Elephant(Animal):
    def make_sound(self):
        return "trumpets!"

    def eat(self):
        return "eats grass and fruits."


class Monkey(Animal):
    def make_sound(self):
        return "chatters!"

    def eat(self):
        return "eats bananas."


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals:
    print(animal.get_name(), animal.make_sound())
    print(animal.get_name(), animal.eat())
    print("-----")
