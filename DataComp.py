# 1. Напишите комбинацию циклов чтобы проитерировать все элементы сложной структуры
# данных вида d = {“a”: {“1”: [...], “2”: [...], ...}, ...} (словарь словарей в которых лежат списки)
# 2. Напишите comprehension, который итерирует строку “1_2,40_5,5_32” (разбить по запятым)
# и каждый элемент разбивает по символу “_” и полученные элементы приводит к типу int,
# и складывает их, тем самым образуя список целых чисел. (Вы можете использовать lambda
# функцию или написать обычную, которая принимает строку вида “1_2” на вход и
# возвращает число как сумму значений из строки; используйте метод split()).

dict = {
    "a": {"1": [1, 2, 3], "2": [2, 3, 4], "3": [3, 4, 5]},
    "b": {"4": [4, "c", "d"], "5": ["a", 5, "b"], "6": ["e", "f", 6]},
    "c": {"7": ["one", "two", "three"], "8": ["four", "five", "six"], "9": ["seven", "eight", "nine"]}
        }

flat = [p for key, val in dict.items() for subkey in key]
print(flat)

# z = []
# def get_data(d):    # метод обращения к сложным данным
#     x = []
#     global z
#     for key, value in d.items():
#         for subkey in key:
#             y = [key, value]
#             x.extend(y)
#             z += value
#     return x
#
#
# s = get_data(dict)
# print(s)
# print(z)







# citys = {"Киев": 4767000, "Одесcа": 2320000, "Днепр": 995000, "Ровно": 457000}
# mega_citys = {}
# for city, val in citys.items():
#     if val >= 1000000:
#         mega_citys.update({city: val})
#
# print(mega_citys)

# mega_citis = {city: val for city, val in citys.items() if val >= 1000000}
# print(mega_citis)
#
# for city in  citys:
#     print(city)
#
# population = 0
# for popul in citys.values():
#     print(popul)
#     population += popul
#
# print(population)
