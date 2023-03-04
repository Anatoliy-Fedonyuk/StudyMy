# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name_getter(self):
#         return self.__name
#
#     @name_getter.setter
#     def name_setter(self, value):
#         self.__name = value
#
#
# user = User(name="Alex")
# print(user.name_getter)
# user.name_setter = "Bob"
# print(user.name_setter)

# class TextProcessor:
#     def __init__(self):
#         self._punktuation = ".,;:\!?#*-"
#
#     def __is_punktuation(self, char):
#         return char in self._punktuation
#
#     def get_clean_string(self, text):
#         clean_text = ""
#         for char in text:
#             if self.__is_punktuation(char):
#                 continue
#             clean_text += char
#         return clean_text
#
#
# # p = TextProcessor()
# # print(p.get_clean_string("Hello; krey-zy, world?!!"))
#
#
# class TextLoader:
#     def __init__(self):
#         self.__text_processor = TextProcessor()
#         self.__clean_string = None
#
#     def set_clean_string(self, text):
#         self.__clean_string = self.__text_processor.get_clean_string(text)
#
#     @property
#     def clean_string(self):
#         print("Clear string is: {}".format(self.__clean_string))
#         return self.__clean_string
#
#
# # t = TextLoader()
# # t.set_clean_string("Hello; krey-zy, world?!\n- stroka: texta...")
# # t.clean_string
#
# class DataInterface:
#     def __init__(self):
#         self.__text_loader = TextLoader()
#
#     def process_texts(self, texts):
#         clean_text = []
#         for text in texts:
#             self.__text_loader.set_clean_string(text)
#             clean = self.__text_loader.clean_string
#             clean_text.append(clean)
#         return clean_text
#
#
# di = DataInterface()
# tx = ["Hello,, I- am Jonh!!?", "Hey... whats?? is the*# wather today-", "Hello; krey-zy, world?!\- stroka: texta..."]
# ct = di.process_texts(tx)
# print(ct)


class A:
    def __init__(self):
        self.__x = 111
        self._y = 33

    def _protected(self):
        print("This Protected method ))")

    def __private(self):
        print("This Private method =)))")

    def stukach(self):
        self.d = self.__x
        return self.__private()


a = A()
print(a._y)
a._protected()
print(a._A__x)
a._A__private()
# print(a.stukach())
# print(a.d)
