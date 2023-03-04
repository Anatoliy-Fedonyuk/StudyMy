# 1. Написать класс Cat, создать ему атрибуты size, color, cat_type.
# 2. При создании объекта класса передавать в конструктор color и cat_type, которые
# записываются в соответсвующие атрибуты.
# 3. Сделать метод set_size, в котором если self.cat_type это “indoor”, то self.size = ‘small’ иначе
# self.size=’undefined’. Протестируйте разные варианты.
# 4. Сделать класс Tiger, унаследованный от класса Cat.
# 5. Переопределить метод set_size таким образом чтобы если self.cat_type это ‘wild’, то self.size
# = ‘big’ иначе self.size=’undefined’.

# class Cat:
#     def __init__(self, color, cat_type):
#         self.color = color
#         self.cat_type = cat_type
#         self.size = "undefined"
#
#     def set_size(self):
#         if self.cat_type != "indoor":
#             self.size = "undefined"
#         else:
#             self.size = "small"
#         return self.size
#
#     @staticmethod
#     def cat_myau():
#         print("Myauuu, Myauuu")
#
#
# Cat.cat_myau()
# cat = Cat(color="white", cat_type="indoor")
# print(cat.set_size())
# print(cat.cat_type)
# print(cat.color)
#
# cat2 = Cat(color="black", cat_type="outdoor")
# print(cat2.set_size())
# print(cat2.cat_type)
# print(cat2.color)
#
#
# class Tiger(Cat):
#     def __init__(self, color, cat_type):
#         super().__init__(color, cat_type)
#
#     def set_size(self):
#         if self.cat_type != "wild":
#             self.size = "undefined"
#         else:
#             self.size = "big big cat!"
#         return self.size
#
#
# tiger = Tiger(color="orange", cat_type="wild")
# print(tiger.set_size())
# print(tiger.cat_type)
# print(tiger.color)
#
# tig = Tiger(color="orange", cat_type="indoor")
# print(tig.set_size())
# print(tig.cat_type)
# print(tig.color)

# from dis import dis  # функция dis
#
# def some(x):
#     return x/5
#
# y = some(125)
# print(y)
#
# var = lambda x: x/5
#
# z = var(125)
# print(z)
#
# print(dis(some))
# print(dis(var))

# 1. Организуйте архитектуру приложения “База данных” (псевдо). В роли базы данных у вас
# будет класс Database, который будет хранить данные в виде переменной списка.
# 2. Класс Database должен иметь методы read_data(criteria), write_data(element).
# 3. Для элемента данных напишите класс Data. В данном случае мы будем хранить данные о
# пользователях. Data будет иметь атрибуты: country, name, age, gender, height, weight.
# 4. В классе Database метод read_data будет принимать на вход аргумент criteria, который
# является словарем вида {“age”: 25}, после чего метод вернет отдельный список всех
# элементов у которых данное условие истино.
# Подсказка: чтобы получить у объекта класса значение его атрибута как у словаря, используйте
# следующий синтаксис: your_class_instance.__dict__.get(‘name’).
# PS: организуйте правильную инкапсуляцию. Вы должны добавлять элементы в класс Database
# только через метод write, но никак не напрямую через атрибут elements.
#   Видимо, имелось ввиду, что в классе Database должна быть переменная класса типа список, например, objects = [],
# в которую должны добавляться экземпляры класса Data("John", 32, 'man', 174, 80), ... .
# Также нужно создать экземпляр класса Database и в методе write_data(...) записать созданные экземпляры класса Data в
# список objects методом append. В методе read_data(...) пройтись по списку объектов objects и в соответствии с criteria
# вернуть из этого метода список с объектами, для которых условие истинно.

xxx = []
class Database:
    def __init__(self):
        self._database = xxx

    def read_data(self, criteria={"age": 25}):
        #        [print(i) for i in self.database if i[2] == criteria.get("age")]  # Чушь
        pass

    def write_data(self, element):
        self._database.append(element)
        # print(self._database)
        return self._database


class Data:
    def __init__(self, name, age, country, gender, height, weight):
        self._database = Database()
        self._name = name
        self._age = age
        self._country = country
        self._gender = gender
        self._height = height
        self._weight = weight
        #
        # def element(self):
        element = tuple((self._name, self._age, self._country, self._gender, self._height, self._weight))
        print(element)
        self._database.write_data(element)


if __name__ == "__main__":
    d1 = Data(name="Alex", age=47, country="Ukraine", gender="male", height=171, weight=85)
    d2 = Data("Romeo", 25, "Moldova", "male", 173, 80)
    d3 = Data("Buyya", 55, "Poland", "male", 178, 86)
    d4 = Data("Linda", 25, "England", "female", 168, 55)
    d5 = Data("Andrew", 15, "Ukraine", "male", 186, 85)
    d6 = Data("Artur", 18, "Brazil", "male", 186, 82)
    d7 = Data("Irina", 35, "Ukraine", "female", 170, 52)
    d8 = Data("Ivana", 28, "Poland", "female", 167, 48)
    d9 = Data("Tanya", 15, "Moldova", "female", 162, 68)

    #    Database().read_data()
    d10 = Database()
    print(d10._database)
#    d1.database.__dict__.get("Ivana")
