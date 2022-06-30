# Object oriented pragramming


# OOP Part -1
print('//////////OOP Part -1')


class Sample():  # Class is used to  define our own object.
    pass

x = Sample()
y = []
print(type(x))  # its type is sample which is declared by us.
print(type(y))  # its type is list which is built-in.

#  OOP Part -2
print('\\\\\\\\\\\\\\ OOP Part -2')


class Dog():

    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog("Husk", "code")
print(my_dog)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)  # Global variable in object. means all dogs are mammals ( Object level variable )


print('\\\\\\\\\\\\ Mathods')

class Circle():
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(99)
print(myc.area())


# OOP Part -3  ( Inheritance and special Methods )
print('\\\\\\\\\\\\\ OOP part -3')

# \\\\\\\\\\\\\ Inheritance
print('\\\\\\\\\\\\\ Inheritance')

class Animal():

    def __init__(self):
        print('Animal Created')

    def Who_am_I(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):  # This class is derived from Animal() Class. Animal is it's parent class.

    def __init__(self):
        # Animal.__init__(self)  # We don't actually need this line to do inheritance
        print("Dog Created")

    def bark(self):  # New methods in derived classes
        print("Woof")

    def eat(self):  # Over writing classes
        print("Dog Eating")


mya = Dog()
mya.eat()
mya.Who_am_I()

# \\\\\\\\\\\\\ Special Methods
print('\\\\\\\\\\\ Special Methods')

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # Special Method to return strings
        return f"Title : {self.title}, Author : {self.author}, pages : {self.pages}"

    def __len__(self):  # Spacial method to define length
        return self.pages

    def __del__(self):  # Spacial method to delete an object
        print("A book is destroyed!")

b = Book("python", "jose", 200)
print(b)
print(len(b))
del b