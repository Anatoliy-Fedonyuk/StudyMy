#   Единое наследование
class Parent:  # Объявление класса
    def __init__(self, name):  # конструктор класса
        self.name = name

    def say_hello(self):  # метод класса Parent
        print("Hello, I am {name}".format(name=self.name))


parent = Parent(name="John")  # Первый объект класса
parent.say_hello()


class Child(Parent):  # Объявление дочернего класса
    def __init__(self, name, age):  # конструктор класса
        super().__init__(name)  # вызов суперкласса , т.е. родительского класса
        self.age = age

    def say_hello(self):  # переопределение метода дочерним классом
        print("Hello, my name is {name} and I am {age} years old".format(name=self.name, age=self.age))


child = Child(name="Mark", age=25)              # Первый объект класса Child
child.say_hello()

#   Множественное наследование
class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 25


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def square_ads(self):       # метод класса C
        print("C class has side A={a_val} and side B={b_val}".format(a_val=self.a, b_val=self.b))

c = C()                 # Первый объект класса C
c.square_ads()

parent = Parent(name="Sarah")            # Второй объект класса
parent.say_hello()

child = Child(name="Neo", age=48)     # Второй объект класса
child.say_hello()