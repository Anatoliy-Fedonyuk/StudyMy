# """Раздел 9
# 9.1 Выражения-генераторы """

# gen = (i for i in range(2, 10001))        # 9.1.1
# print(*gen)

# a, b = map(int, input().split())
# tp = tuple(x**2 for x in range(a, b+1))
# print(tp)

# a, b = map(int, input().split())             # 9.1.3
# print(*(abs(x) for x in range(a, b+1)[0:5]), sep='\n')

# gen = (i for i in range(100))
# d = dict()
# print(d.fromkeys((gen), 0))
# # max(gen)
# # sum(gen)
# # min(gen)

# a = int(input())             # 9.1.6
# print(*(abs(x)**3 for x in range(-a, a+1)[:4]))

# from string import ascii_lowercase          # 9.1.7
#
# # gen = (i + j for i in ascii_lowercase for j in ascii_lowercase)
# print(*list(i + j for i in ascii_lowercase for j in ascii_lowercase)[:50])

# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# print(*tuple(j for i in range(1_000_000) for j in cities)[:20])


# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]        # 9.1.8 ver
# gen = (cities[i % len(cities)] for i in range(1_000_000))
# print(*(next(gen) for i in range(20)))


# a, b = map(int, input().split())             # 9.1.9
# gen = (0.5*pow((i/100),2)-2 for i in range(100*a, 100*b+1))
# print(*(round(next(gen), 2) for i in range(20)))

# ФУНКЦИИ ГЕНЕРАТОРЫ, YIELD!

# def get_list():               # lesson
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a)/len(a)
#
# a = get_list()
# print(tuple(a))
# a = get_list()
# print((*a,))
# a = get_list()
# print(list(a))
# a = get_list()
# print([*a])

# def get_sum(n):               # 9.2.1
#     for i in range(1, n+1):
#         yield sum(range(1, i+1))

# N = int(input())
# gen = get_sum(N)
# print(list(gen))

# print(*(get_sum(int(input()))))


# def tribon(n):        # 9.2.2
#     a, b, c = 1, 1, 1
#     for _ in range(n):
#         yield a
#         a, b, c = b, c, a + b + c
#
# N = int(input())
# print(*tribon(N))


# trib = lambda n: trib(n-1) + trib(n-2) + trib(n-3) if n > 3 else 1
# [print(trib(i), end=' ') for i in range(1, int(input())+1)]


# import random
# from string import ascii_lowercase, ascii_uppercase
#
# random.seed(1)
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#
# def randomizer(n, par=""):
#     for i in range(n):
#         par += chars[random.randint(0, len(chars))]
#     yield par
#
# N = int(input())
# for j in range(5): print(*randomizer(N))


# from random import seed, choice        # 9.2.4
# from string import ascii_lowercase, ascii_uppercase
# seed(1)
# chars = ascii_lowercase + ascii_uppercase
#
# def gen_e_mail(n):
#     while True: yield ''.join(choice(chars) for _ in range(n)) + '@mail.ru'
#
# gen = gen_e_mail(int(input()))
# [print(next(gen)) for _ in range(5)]

# def gen_prime(n=2):                # 9.2.5 Генератор простых чисел - падло))
#     while True:
#         count = 0
#         for i in range(2, n):
#             if not (n % i): count += 1
#         if not count: yield n
#         n += 1
#
# gen = gen_prime()
# [print(next(gen), end=" ") for _ in range(20)]

# ФУНКЦИЯ MAP!

#  функция Мап может и с несколькими массивами работать! при чем разной длины! в данном случае хвосты Мап сама откинула..
# l1 = [1, 2, 4, 6, 4]
# l2 = [3, 4, 5, 6, 4, 5, 4]
# l3 = [1, 4, 6, 9]
# a = list(map(lambda x1, x2, x3: x1 + x2 + x3, l1, l2, l3))
# print(a)


# print(*list(map(float, input().split()))[:3])

# print(*map(lambda x: abs(int(x)), input().split()))       # 9.3.2
#
# import sys                                            # 9.3.3
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst2D = [[*map(int, i.split())] for i in lst_in]
# lst2D = [*map(lambda x: [*map(int, x.split())] ,lst_in)]
# print(lst2D)

# s = input()
# s_lst = s.split()
# tp = tuple(map(lambda x: tuple(x.split("=")), s_lst))
# print(tp)
# # tp = tuple(tuple(j.split("=")) for j in s)

#                   9.3.5
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# print(''.join(map(lambda x: t.get(x, "-"), input().lower())))


# print(*map(lambda x: (x if len(x) > 5 else "-"), input().split()))


# ФУНКЦИЯ FILTER !!!!!

# b = filter(lambda x: not x % 2, range(11))
# print(*b)
# print(*filter(None, [2, -9, "8", True, False, "sjd", [], 0, 0.9, 0.0, "Ф", '']))

# def is_prime(x):
#     return not len([c for c in range(2, x) if not x % c]) and x > 1

# def is_prime(x):
#     return not any(c for c in range(2, x) if not x % c) and x > 1
# print(*filter(lambda x: x % 2, filter(is_prime, range(20))))

# print(*filter(lambda x: not any(c for c in range(2, x) if not x % c) and x > 1, range(20)))

# 9.4.1
# f = filter(lambda y: len(y) > 5, input().split())
# print(next(f), next(f), next(f))


# import sys          # 9.4.2 мое
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# tp = tuple(map(lambda x: tuple(x.split("=")), lst_in))
# print(*(y[0] for y in filter(lambda x: int(x[1]) >= 500, tp)))

# print(*filter(lambda z: len(str(abs(z)))==2, map(int, input().split())))

# 9.4.4 мое
# a, b = set(map(int, input().split())), set(map(int, input().split()))
# print(*filter(lambda v: not v % 2, sorted(a & b)))

# ch = set('abcdefghijklmnopqrstuvwxyz0123456789.@_')          # 9.4.5 мое
# print(*filter(lambda x: set(x)|ch == ch and "." in x[x.index("@"):-2], input().lower().split()))

# ФУНКЦИЯ ZIP !!!!!

# a = ((1,2,3,4),(2,3,4,5),(3,4,5,6))
# b = tuple(zip(*a))
# print(b)

# a, b = [*map(int, input().split())], [*map(int, input().split())]       # 9/5/1
# print(*[*map(lambda x: x[0]*x[1], zip(a, b))][:3])

# import sys                       # 9/5/2
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# t2D = (*map(lambda x: tuple(map(int, x.split())) ,lst_in), )
# [print(*x) for x in tuple(zip(*zip(*t2D)))]

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(*zip(*zip(*lst_in)))
# [print(*c, sep='') for c in zip(*zip(*lst_in))]

# [*map(print, *zip(*map(str.split, map(str.strip, open(0)))))]  # Not my, but wery strong

# [print(*x) for x in zip(*map(str.split, map(str.strip, open(0))))]   # 9/5/3


# [print(*x) for x in zip(*[iter(input().split())]*3)]       # 9/5/4

# x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(*zip(x, x, x))

# s = input(); lst = list(zip(s, range(10)))       # 9/5/5

# ФУНКЦИЯ SORTED и метод SORT

# lst = [*map(int, (s := input()).split())]     # 9.6.2
# lst.sort(); tp_lst = (*sorted(lst),)
# print(lst)
# print(tp_lst)
# print(s)


# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# def get_sort(d):
#     return [*dict(sorted(d.items(), reverse=True)).values()]
# def get_sort(d):
#     return [*dict(sorted(d.items())[::-1]).values()]
# print(get_sort(d))
# print(dict(sorted(d.items())[::-1]))
# print(dict(sorted(d.items())))

# print(*sorted(set(map(int, input().split())))[:-5:-1])     # 9.6.4

# a, b = [*map(int, input().split())], [*map(int, input().split())]       # 9.6.5
# print(*[*map(lambda x: sum(x), zip(sorted(a), sorted(b)[::-1]))])

# import sys      # 9.6.6 my
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {int(i.split(":")[1]):i.split(":")[0] for i in lst_in}
#
# def dict_sort(d):
#     d = (dict(sorted(d.items())))
#     return list(d.values())[:3]
#
# print(*dict_sort(d))


# import sys
# my_dict = {int(k): v for v, k in [c.strip().split(':') for c in sys.stdin.readlines()]}
# print(my_dict)
#
# def min_price(d: dict) -> list:
#     return [d[key] for key in sorted(d)][:3]
#
# print(*min_price(my_dict))

#  АРГУМЕНТ KEY ДЛЯ СОРТИРОВКИ! ф-я REDUCE !!!!!

# a = [4, 301111, -10, 158, 7, 12, 33, -45, 77, 113]
# b = sorted(a, key=lambda x: (x % 2, len(str(abs(x))), x))
# print(b)

# print(*sorted(input().split(), key=lambda x: 1/len(x)))      # 9.7.1
# print(*sorted(input().split(), key=len)[::-1])

# import sys
# d = {int(k): v for v, k in [c.strip().split('=') for c in sys.stdin.readlines()]}
# print(*[d[key] for key in sorted(d, key=lambda x: -x)])


# d = dict(map(lambda x: x.strip().split('='), __import__('sys').stdin))      # 9.7.2
# print(*sorted(d, key=lambda x: -int(d[x])))

# print(*sorted(input().split(), key='доремифасольляси'.index))      # 9.7.3

# n=(1,2,0)             # Работа с матрицей - сортировкой индексов
# a=(("a","b","c"),("d","e","f"),("j","i","l"))
# [print(r) for r in a]
# a = tuple(zip(*a))
# print(a)
# b = sorted(a, key=lambda x: n.index(a.index(x)))
# a = tuple(zip(*b))
# [print(r) for r in a]


# lst_in = list(map(str.strip, __import__('sys').stdin))                                       # 9.7.4 !!!
# t = tuple(zip(*[[int(s) if s.isdigit() else s for s in x.split(';')] for x in lst_in]))
# t_sorted = tuple(zip(*sorted(t, key=lambda x: (1,3,2,0).index(t.index(x)))))
# [print(r) for r in t_sorted]


# lst_in = list(map(str.strip, __import__('sys').stdin))
# rank = ('рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник')
# lst = sorted((i.split("=") for i in lst_in), key=lambda x: rank.index(x[-1]))
#
# print(lst)


#  Функция ISINSTANCE() , TYPE()

# def get_add(a, b):                                          # 9.8.2 my
#     if type(a) in (int, float) and type(b) in (int, float):
#         return a + b
#     elif isinstance(a, str) and isinstance(b, str):
#         return a + b
#
# print(get_add([0, 1, 3], -23))

# def get_add(a, b):          # genius
#     tset = {type(a), type(b)}
#     if tset <= {int, float} or tset == {str}:
#         return a + b

# def get_sum(it): return sum(filter(lambda x: type(x) is int, it))                             # 9.8.3 my
# print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))

# def get_even_sum(it): return sum(filter(lambda x: (type(x) is int and not x % 2), it))
# print(get_even_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))


# def get_list_dig(lst): return [*filter(lambda x: type(x) in (int,float), lst)]                  # 9.8.5 my
# print(get_list_dig([1,2,3, "a", True, [4, 5], "c", (4, 5)]))

#  ФУНКЦИИ ALL & ANY

# print(any([]))
# print(all([]))

# print(all(not x%2 for x in map(int, input().split())))                              # 9.9.1

# print(any(float(x)<0 for x in input().split()))                              # 9.9.2

# def is_string(lst): return all(map(lambda y: type(y) is str, lst))               # 9.9.3

# print(("учится", "отчислен")[any(int(x)<3 for x in input().split())])               # 9.9.4

# ls = [['x','o','x'],['x','#','x'],['o','x','o']]
# def is_free(lst): return any("#" in r for r in lst)
# print(is_free(ls))

# Задания для самоподготовки
# 1. Напишите программу ввода натуральных чисел через запятую и преобразования этой строки в список целых чисел.
# (Используйте здесь функцию map для преобразования элементов последовательности строк в последовательность чисел).
# Реализовать обработку возможных исключений при таком преобразовании.
#
# 2. Написать функцию вычисления среднего арифметического элементов переданного ей списка. Реализовать обработку
# возможных исключений при ее работе.
#
# 3. Написать функцию-генератор (с использованием оператора yield) для удаления произвольного элемента из множества
# (с помощью метода pop()). Функция должна возвращать значение удаленного элемента. Реализовать обработку возможных
# исключений при ее работе.

# 1
# try:
#     print("Введите список натуральных, целых чисел - через запятую! :")
#     lst_res = [*map(int, input().split(","))]
# except BaseException as E:
#     lst_res = E
# finally:
#     print("Выведем ни смотря ни на что")
#
# print(lst_res)

# 2
# def average(ls: list[int | float]) -> float:
#     try:
#         return sum(ls)/len(ls)
#     except ZeroDivisionError as Z:
#         print(Z, "Вводимый список не должен быть пустым!")
#     except TypeError as T:
#         print(T, "Список должен содержать только числовые значения!")
#
# lst = True, False, 0
# print(average(lst))

# # 3
# def func_pop(st) -> object:
#     yield st.pop()
#
#
# ss = {22, 'sd', -3, 0, None}
# a = func_pop(ss)
# print(*a)
# print(*a)

# ФУНКЦИЯ ENUMERATE !!!!!!!!!!!!
# def enumerate(sequence, start=0):     # ее работа такая!
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1


# for i, l in enumerate("hello", 1):
#     print(l, i)
#
# c = {'d': 'a', 'dd': 'b', 'ddd': 'c'}
# for i in enumerate(c):
#     print(i)
#
# s = {-7, 0.0, 9, 33, -23, 11.1}
# for i in enumerate(s, 1):
#     print(i)

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]       # 1 for enumerate
# AA = [[0 if i is j else x for i, x in enumerate(row)] for j, row in enumerate(A)]
# [print(*r) for r in AA]

# Написать свою функцию enumerate, которая бы для словарей возвращала кортеж из трех значений:
# (индекс, ключ, значение)
# Для остальных коллекций работала бы без изменений.

# def enumerate(sequence, start=0):
#     n = start
#     match sequence:
#         case dict(sequence):
#             for elem in sequence:
#                 yield n, elem, sequence[elem]
#                 n += 1
#         case _:
#             for elem in sequence:
#                 yield n, elem
#                 n += 1
#
# c = {'d': 'a', 'dd': 'bb', 'ddd': 'ccc'}
# s = {-7, 0.0, 9, 33, -23, 11.1}
# l = [-7, 0.0, 9, 33, -23, 11.1]
# st = 'very nice day'

# for i in enumerate(st, 1): print(i)

# Написать свою функцию enumerate, которая бы позволяла одним циклом for перебирать двумерные
# (вложенные) упорядоченные списки (как в подвиге 1) и возвращала кортеж из трех значений:
# (строка, столбец, значение)
# def enumerate_matrix(sequence):
#     n, m = 1, 1
#     for row in sequence:
#         for x in row:
#             yield m, n, x
#             n += 1
#         m += 1
#         n = 1
#
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# for i in enumerate_matrix(A): print(i)

# # 3 TRY/EXCEPT/FINALLY
# def func_pop(st) -> object:
#     try:
#         yield st.pop()
#         # raise KeyError
#     except IndexError as IE:
#         print(IE, "Нельзя pop из пустого множества")
#     except KeyError as KE:
#         print(KE, "Нельзя удалить значение из пустого множества")
#
#
# ss = {22, 'sd', -3, 0, None}
# for x in range(len(ss)):
#     d = func_pop(ss)
#     print(*d)
# d = func_pop(ss)
# print(*d)