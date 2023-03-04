# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         print("work Getter")
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         print("work Setter")
#         if new_age > 0 and new_age == int(new_age):
#             self.__age = new_age
#         else:
#             print("Enter the correct age!")
#
#
# us = User("Vasya", 35)
# print(us.name, us.age)
# us.age = 48
# print(us.name, us.age)


def function(data, new_value):  # полиморфизм - перегрузка метода
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, tuple):
        if isinstance(new_value, tuple):
            data += new_value
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


# print(function([1, 3, 7], 8))
# print(function((1, 3, 7), (8, 6)))
# print(function({1, 0, 8, 31}, 8))
# print(function("adhadj", "55"))


# 1. Написать класс User, у него будут в конструкторе определяться поля age, name, user_type,
# а метод будет access_database.
# 2. Сделать метод таким, чтобы если self.user_type был равен “superuser”, то метод выводил в
# консоль “access granted”, в случае если это просто юзер, то выводило “access denied”.
# 3. Для суперюзера сделать унаследованный класс SuperUser от User.

# class User:       # полиморфизм - перегрузка метода
#     def __init__(self, age, name, user_type="user"):
#         self._age = age
#         self._name = name
#         self.user_type = user_type
#
#     def access_database(self):
#         if self.user_type == "superuser":
#             print("Access granted ! \n Your name - {name} and your {age} y.o.".format(name=self._name, age=self._age))
#         elif self.user_type == "user":
#             print("Access denied")
#         else:
#             print("enter the correct value user_type")
#
# us1 = User(35, "Vasya", "user")
# us2 = User(51, "Ivan", "superuser")
# us3 = User(99, "Io", "superuser")
# us4 = User(44, "Petya")
#
# us1.access_database()
# us2.access_database()
# us3.access_database()
# us4.access_database()

class User:
    def __init__(self, age, name, user_type="user"):
        self._age = age
        self._name = name
        self.user_type = user_type

    def access_database(self):
        print("Access denied")


class SuperUser(User):
    def access_database(self):
        if self.user_type == "superuser":
            print("Access granted ! \n Your name - {name} and your {age} y.o.".format(name=self._name, age=self._age))
        else:
            print("Access denied")


us1 = User(35, "Vasya", "user")
us2 = SuperUser(51, "Ivan", "superuser")
us3 = SuperUser(99, "Io", "superuser")

us1.access_database()
us2.access_database()
us3.access_database()
