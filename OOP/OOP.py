# classes are blueprints that can be instantiated into instances of objects

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):  # self refers to itself
        if age > 18:
            self._name = name  # attributes
            self._age = age  # _means that its a private variable as a convention standard but its no guarantee

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print('run')
        return 'done'

    @classmethod  # can be used without instantiating a class, clas method, not used often, when we care about class attributes
    def adding_things(cls, num1, num2):  # cls stands for class
        return cls('Teddy', num1 + num2)  # used to instantiate an object

    @staticmethod  # dont care about the class attributes/state
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 20)
player2 = PlayerCharacter('Bob', 30)
player3 = PlayerCharacter.adding_things(2, 3)


# pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism
# Encapsulation - creating classes that have attributes
# Abstraction - hiding information and giving access to only what's necessary (private vs public)
# Inheritance - allows new objects to take on the properties of existing objects
# Polymorphism - object classes can share the same method name but method names can act different based on what object calls them
class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)

print(hb1.attack())

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.check_arrows()
print(isinstance(wizard1, Wizard))  # checks is an instance of
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))  # object is always the parent class of every object made


# dunder methods - you can redefine built in object methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted!')

    def __call__(self):  # calls the object
        return ('yess?')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del(action_figure)
print(action_figure())  # call
print(action_figure['name'])


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))

#MRO - method resolution order - checks depth first search for what order you are inheriting, use __mro__