# Animal is-a object
class Animal(object):
    @staticmethod
    def latin_name():
        return "Animal"


# Dog is-a Animal
class Dog(Animal):

    # Dog has-a name
    def __init__(self, name):
        self.name = name

    def eater(self):
        return "Carnivore", Animal.latin_name(), self.name


# Cat is-a Animal
class Cat(Animal):

    # Cat has-a name
    def __init__(self, name):
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # person has-a name
        self.name = name

        # person has-a Pet of some kind
        self.pet = None


# Employees are people
class Employee(Person):

    def __init__(self, name, salary):
        # call constructor of super class
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass

# Rover is-a dog
rover = Dog("Rover")

# Satan is-a cat
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# Mary has-a pet - cat Satan
mary.pet = satan

# Fran is-a employee with a salary of ...
frank = Employee("Frank", 12000)

# Frank has-a pet rover
frank.pet = rover

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

print rover.eater()
