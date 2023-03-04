# class Base:  # полиморфизм - метод перегрузки
#     def __init__(self, a):
#         self.a = a
#
#     def print_a(self, square=False, multi=None):
#         if square and not multi:
#             print(self.a ** 2)
#         elif not square and multi:
#             print(self.a * multi)
#         elif square and multi:
#             print((self.a ** 2) * multi)
#         else:
#             print(self.a)
#
#
# base = Base(5)
# base.print_a(square=True)
# base.print_a(multi=7)
# base.print_a(square=True, multi=2)
# base.print_a()


# class Multiplier:       # полиморфизм - переопределение метода
#     def __init__(self, a):
#         self.a = a
#
#     def print_a(self, x):
#         print(self.a * x)
#
#
# class Exponent(Multiplier):
#     def print_a(self, x):
#         print(self.a ** x)
#
#
# mu = Multiplier(3)
# mu.print_a(7)
# expo = Exponent(5)
# expo.print_a(3)


class Animal:       # полиморфизм - переопределение метода
    def __init__(self, name):
        self._name = name

    def voice(self):
        print("Rrrrr")


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("Bark")


# animal = Animal("?")
# animal.voice()
# cat = Cat("Sarah")
# cat.voice()
# dog = Dog("Rex")
# dog.voice()

class Animal2:      # полиморфизм - перегрузка метода
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == "cat":
            print("Meow")
        elif self._name == "dog":
            print("Bark")
        else:
            print("Rrrr")


a1 = Animal2("cat")
a2 = Animal2("dog")
a3 = Animal2("dinozaurus")
a1.voice()
a2.voice()
a3.voice()
