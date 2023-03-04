# from math import ceil, pi
# import time
# import pprint
# import random


# # print(locals())
# pprint.pprint(locals())
# print(a := ceil(1.8))
# print(pi)

# Битовые операции 10.2

# n = int(input())
# n |= 0b00001000
# print(n)
# аналог
# print(int(input()) | 0b0001000)
# print(int(input()) | (1 << 3))
# print(1 << 3)
# print(bin(1))
# print(bin(1 << 3))

# def off_bit(numbers, bit_off): return numbers | 1<<bit_off
# включение
# print(off_bit(100, 3))

# выключение
# print(int(input()) & ~0b00010010)
# print(int(input()) & ~(1<<4) & ~(1<<1))

# переключение
# print(int(input()) ^ (1<<3) ^ (1))

# умножить на 4 битово
# print(int(input()) << 2)

# 10.2.7 !
# st = 'ѩкю[щюлцхZ'
# key = 123
# print("".join(chr(ord(i) ^ 123) for i in input()))

# n, mask = int(input()), (1<<6 | 1<<3)               # 10.2.8
# print("ДА" if n & mask == mask else "НЕТ")

# print('НДЕАТ'[int(input())&72==72::2])      # Оригинальная печать по срезу))

# n = int(input()); print('НДЕАТ'[n&(1<<5)==(1<<5) or n&(1<<1)==(1<<1)::2])
#
# print('НДЕАТ'[int(input()) & 34 > 0::2])     # Оригинальное решение но верное))

# print(('НЕТ', 'ДА')[bool(int(input()) & (1 << 5 | 1 << 1))])
#
# print('НДЕАТ'[int(input())&(1<<5 | 1<<1) > 0::2])               # 10.2.9 как ни странно все рабочие)

# print('НДЕАТ'[bool(int(input())&(1<<5 | 1<<1))::2])


# Module RANDOM !!!!

# print(random.random())
# print(random.uniform(-23, 232))
# print(random.randint(-23, 23))
# print(random.randrange(-3, 10, 2))
# print(random.randrange(10))
# print(random.gauss(1, 3.5))
# lst = [4,5,0,-3,10,76]
# print(lst)
# print(random.choice(lst))
# random.shuffle(lst)
# print(lst, "lst after shuffle")
# print(random.sample(lst, 3))
#
# random.seed(123)
# print([random.randint(0, 10) for i in range(20)])


# import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# a, b = map(int, input().split())
# random.seed(1)
# print(round(random.uniform(a, b), 2))                     # 10.3.2

# print(round(random.uniform(*map(int, input().split())), 2))

# import random; random.seed(1)
# __import__('random').seed(1)                    # 10.3.3
# print(random.randint(*map(int, input().split())))

# import random; random.seed(1)
# print(random.choice(input().split()))


# from random import seed, shuffle; seed(1)                           # 10.3.5 !!переворот матрицы - шафлом смешиваем строки и опять транспонируем)
# t = [*zip(*map(str.split, map(str.strip, __import__('sys').stdin)))]
# shuffle(t)
# [print(*x) for x in list(zip(*t))]

# from random import seed, sample; seed(1)
# print(*sample(input().split(), 3))


# from random import seed, randrange; seed(1)             #finaly my)
# N = int(input())
# P = [[0] * N for i in range(N)]
#
# M = 10
# while M:
#     row = randrange(0, N, 2)
#     col = randrange(0, N, 2)
#     if P[row][col] == 0:
#         P[row][col] = 1
#         M -= 1
#
#
# [print(*r) for r in P]


# from random import seed, randint; seed(1)
# N = int(input())
# P = [[0] * (N+2) for i in range(N+2)]
#
# M = 10
# while M > 0:
#     row = randint(1, N)
#     col = randint(1, N)
#
#     if P[row][col] + P[row + 1][col] + P[row - 1][col] + P[row][col + 1] + P[row][col - 1] + P[row + 1][col + 1] + P[row + 1][col - 1] + P[row - 1][col + 1] + P[row - 1][col - 1] == 0:
#         P[row][col] = 1
#         M -= 1
#
#     else:
#         continue
#
# P = list(i[1:-1] for i in P[1:-1])
# [print(*r) for r in P]

# def heron(a, b, c):
#     return round(sum([a, b, c])/2, 2)
#
# print(heron(3,4,5))

# def grow(arr):
#     g = 1
#     for i in arr:
#         g *= i
#     return g
#
# print(grow([1,2,3,4,]))


# list1 = [
#   { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
#   { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
#   { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'JavaScript' },
# ]
# def is_same_language(lst):
#     s = []
#     for j in lst:
#         s.append(j.get('language'))
#     return len(set(s)) == 1
#
# print(is_same_language(list1))

# def even_chars(st):
#     return "invalid string" if len(st) < 2 or len(st) > 100 else list(st)[1::2]
# print(even_chars("a"))

# def to_float_array(arr):
#     return [*map(float, arr)]
# print(to_float_array(["1", "2", "3"]))

# def isPalindrome(x):
#     return str(x) == str(x)[::-1]
#
# print(isPalindrome(11))

# class Solution:
#     def isPalindrome(self, x):
#         if x > 0:
#             temp = x
#             rev_int_elements = []
#             while temp > 0:
#                 digit = temp % 10
#                 rev_int_elements.append(digit)
#                 temp = temp // 10
#             org_int_elements = rev_int_elements[::-1]
#             return rev_int_elements == org_int_elements
#         elif x == 0:
#             return True
#         else:
#             return False
#
#
# sol = Solution()
# print(sol.isPalindrome(121))


# class Solution(object):
#     def shuffle(self, a: list[int], n: int) -> list[int]:
#         return [y for row in [list(x) for x in zip(a[:n], a[n:])] for y in row]
#

# import itertools
# class Solution:
#     def shuffle(self, a: list[int], n: int) -> list[int]:
#         print(*zip(a[:n], a[n:]))
#         return [*itertools.chain(*zip(a[:n], a[n:]))]
#

# class Solution:
#     def shuffle(self, nums: list[int], n: int) -> list[int]:
#         result = [0] * (2 * n)
#         for i in range(n):
#             result[2 * i] = nums[i]
#             result[2 * i + 1] = nums[n + i]
#         return result
#
# sol = Solution()
# print(sol.shuffle([1,2,3,4,4,3,2,1], n=4))


# # s = "LVIII"                   # Перевод числа из римского в десятичное ))
# s = "MCMXCIV"
# d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# n = [d[j] for j in s] + [0]
# print(sum([-n[i] if n[i] < n[i+1] else n[i] for i in range(len(n)-1)]))


# nums = [3,2,4]
# tar = 6
# def twoSum(nums, target):
#     for j in range(len(nums)):
#         for i in range(j+1, len(nums)):
#             if nums[j] + nums[i] == target:
#                 return [j, i]
#
#
# print(twoSum(nums, tar))
#
#
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i
#             print(hashmap)
#
#
# sol = Solution()
# print(sol.twoSum([2,7,11,15], 9))

# АННОТАЦИИ ТИПОВ
# from typing import Any, Callable, Union, Optional, Final, Type, TypeVar

# tr: dict = {'car': 'машина'}
#
# a: Any = None
# s: str = "123"
# s = a
#
# class Geom: pass
#
# class Point2D(Geom):
#     x: int
#     y: int
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#
#     def copy(self) -> "Point2D":
#         return Point2D(self.x, self.y)
#
#
# p = Point2D(10, 20)
#
#
# T = TypeVar("T", bound=Geom)
#
# def factory_object(cls_obj: Type[T]) -> T:
#     return cls_obj()
#
# geom: Geom = factory_object(Geom)
# point: Point2D = factory_object(Point2D)

# КОНСТРУКЦИЯ MATCH/CASE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# lang = input("Какой язык программирования будем учить? \n")
#
# match lang:
#     case "JavaScript":
#         print("Ты можешь стать фронтэнд разработчиком")
#     case "Python":
#         print("Ты можешь стать Data Scientist-ом")
#     case "PHP":
#         print("Ты можешь стать бэкенд разработчиком")
#     case "Solidity":
#         print("Ты можешь стать Blockchain разработчиком")
#     case str("Java") if 3 < len(lang) < 5:
#         print("Ты можешь стать мобильным разработчиком")
#     case  _:
#         print("Язык не важен, главное уметь решать задачи)")


# num = int(input())
# match num:
#     case 1 | 2 | 3 | 4 | 5:
#         print(("Совсем еще зеленый студентик", "Джун-студент", "Мидл-студент", "Сеньер-студент", "Босс качалки")[num-1])
#     case _: print("Неизвестный курс")


# n = int(input())
# match n:
#     case int() as num if 0 < num < 13:
#         print([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][num-1])
#     case _: print("Неверный ввод")


# match input().capitalize():
#     case 'Овен' | 'Лев' | 'Стрелец': print("Огненный")
#     case 'Телец' | 'Дева' | 'Козерог': print("Земной")
#     case 'Близнецы' | 'Весы' | 'Водолей': print("Воздушный")
#     case 'Рак' | 'Скорпион' | 'Рыбы': print("Водный")
#     case _: print("Неверный ввод зодиака")


# value = [1, 2, 3]
#
# match value:
#     case int() | float():
#         print("Имеем дело с числом")
#     case str():
#         print("Имеем дело со строкой")
#     case list():
#         print("Имеем дело со списком")
#     case  _:
#         print(f"Лучше с этим дел не иметь")


# match int(input()):
#     case n if not n % 15: print("FizzBuzz")
#     case n if not n % 5: print("Buzz")
#     case n if not n % 3: print("Fizz")
#     case _: print(n)


# print("Fizz" * (not (n := int(input())) % 3) + "Buzz" * (not n % 5) or n)

# print((3, 2, 0)[len({int(input()), int(input()), int(input())})-1])

# match {int(input()) for i in "..."}:
#     case mn if len(mn) == 1: print(3)
#     case mn if len(mn) == 2: print(2)
#     case _: print(0)

# month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
#          7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
# match int(input()):
#     case m if 0 < m < 13: print(month.get(m))
#     case _: print("некорректный номер месяца")

# num = int(input())
# old = {'Младенец': 0 <= num < 2, 'Малыш': 2 <= num < 4,
#      'Ребенок': 4 <= num < 12, 'Подросток': 12 <= num < 19,
#      'Взрослый человек': 19 <= num < 65, 'Пожилой человек': num >= 65}
# [print(key) for key, value in old.items() if value]

# print(('Пожилой человек', 'Взрослый человек', 'Подросток', 'Ребенок', 'Малыш', 'Младенец')
#       [((n := int(input())) < 2) + (n < 4) + (n < 12) + (n < 19) + (n < 65)])

# n = int(input())
# print('Младенец' if n < 2
#       else 'Малыш' if n < 4
#       else 'Ребенок' if n < 12
#       else 'Подросток' if n < 19
#       else 'Взрослый человек' if n < 65
#       else 'Пожилой человек')

# match int(input()):
#       case age if age < 2: print('Младенец')
#       case age if age < 4: print('Малыш')
#       case age if age < 12: print('Ребенок')
#       case age if age < 19: print('Подросток')
#       case age if age < 65: print('Взрослый человек')
#       case _: print('Пожилой человек')

# x, y = float(input()), float(input())
# match op := input():
#       case op if op in '+': print(x + y)
#       case op if op in '-': print(x - y)
#       case op if op in '*': print(x * y)
#       case op if op in '/' and y != 0: print(x / y)
#       case _: print('Неизвестно')


# try:
#     a, b, s = float(input()), float(input()), input()
#     if s not in '+-*/':
#         raise ValueError
#     print(eval(f'{a} {s} {b}'))
# except (ZeroDivisionError, ValueError):
#     print("Неизвестно")

# x, y = float(input()), float(input())
# match op := input():
#       case op if op in '+-': print((op=='+')*(x + y) + (op=='-')*(x - y))
#       case op if op=='*' or op=='/' and y: print((op=='*')*(x*y) + (op=='/')*(x/y))
#       case _: print('Неизвестно')

# try:
#       a, b, s = input(), input(), input()
#       print((eval(f'{a} {s} {b}')) if s in '+-*/' else "Неизвестно")
# except (ZeroDivisionError, ValueError): print("Неизвестно")


# a, b, s = input(), input(), input()
# match s:
#       case s if s in '+-*': print(float(eval(a+s+b)))
#       case s if s in '/' and float(b): print(float(eval(a+s+b)))
#       case _: print('Неизвестно')

# def factorial(n):
#       if n <= 0:
#             return 1
#       return n * factorial(n - 1)
#
# print(factorial(6))

# class A:
#       def __init__(self):
#             self.x = 1
#             self.__y = 1
#
#       def getY(self):
#             return self.__y
#
# a = A()
# print(a.x)
# a.x = 45
# print(a.x)

# x, y, z = True, False, True
#
# if not x or y: print(1)
# elif not x or not y and z: print(2)
# elif not x or y or not y and x: print(3)
# else: print(4)

# class parent:
#     def __init__(self, param):
#         self.v1 = param
#
# class child(parent):
#     def __init__(self, param):
#         self.v2 = param
#
# obj = child(11)
# print("%d" % (obj.v2))

# n = set([1,1,1,2,2,2,3,3,3,4,4,4,4])
# print(len(n))

# l1 = [1,3]
# l2 = l1
# l1[0] = 4
# print(l2)


# match input(), input():
#       case k if len(k[0]) < 7: print("Short")
#       case k if len(set(k))==2: print("Difference")
#       case _: print('OK')

# print(('Short',"Difference",'OK')[(len(x := input()) < 7, x != input(), 1).index(1)])

# print((x := int(input()))*2, x/2, sep='\n')
# print((a := float(input()))**2)
# print(int(input())+int(input()))
# print((a:=float(input())) * (b:=float(input())), 2*(a + b))
# print((float(input())-32)*5/9)
# print(abs(int(input()))+abs(int(input())))
# x1, x2 = float(input()), float(input())
# print(abs(float(input()) - float(input())))
# print(round(x := float(input()), 2), round(x, 3))

# h1, m1, s1, h2, m2, s2 = (int(input()) for i in range(6))
# print(s2 - s1 + (m2 - m1) * 60 + (h2 - h1) * 3600)

# a, b, c = (int(input()) for i in "fun")
# print(max(a+b+c, a*b*c, a+b*c, a*b+c, (a+b)*c, a*(b+c)))

# ls = [*map(int, input().split())]
# print(sum(ls)/len(ls))

# print(max([*map(int, input().split())]))
# print(max(input().split(), key=int))

# n, a, b = map(int, input().split())
# print(n * 2 * a * b)

# s = int(input())
# print(int(s/6), int(2*s/3), int(s/6))

# print((lambda x, y, z: x*3 + y*5 + z*12)(*map(int, input().split())))
# print((a := [*map(int, input().split())])[0]*3 + a[1]*5 + a[2]*12)

# a, b = map(int, input().split())
# print((l := [*map(int, input().split())])[1]-1, l[0]-1)
# print(*[*map(lambda x: int(x)-1, input().split())][::-1])
# (lambda x, y: print(y-1, x-1))(*map(int, input().split()))

# print(input().replace(' ', ','))

# (lambda n: print(n-1, n, n+1, sep='<'))(int(input()))

# print("---".join(input() for i in 'o_0'))

# print(*range(1, 6), sep=(input()))
# print(input(), end=" - Сказала она!")

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# n, k = int(input()), int(input())
# print(k//n)
# print(int(input())//int(input()))
# print((n:=int(input()))//100 % 10 + n//10 % 10 + n % 10)
# print((lambda n: n%10 + n//10%10 + n//100)(int(input())))
# print(int((x := input())[0]) + int(x[1]) + int(x[2]))

# print(sum(map(int,input())))          # 1.8.6

###     ПОДСЧЕТ КОЛИЧЕСТВА КУПЮР НА ДАННУЮ СУММУ ИЗ НОМИНАЛОВ В СПИСКЕ
# print(sum([(n:=int(input()))//100, n%100//20, n%20//10, n%10//5, n%5]))         #Primitive

# n, s, k, d = int(input()), [100,20,10,5,1], [], {}                     #my 1
# for i in range(len(s)):
#     k.append(n//s[i])
#     n -= k[i]*s[i]
#     d[s[i]] = k[i]
# print(sum(k))
# print(d)

# n, s = int(input()), [100**100,100,20,10,5,1]                #my 2 Я прям супер)) а словарь оч.полезен!
# d = {s[i]: n%s[i-1]//s[i] for i in range(1,len(s))}
# print(sum(d.values()))

# n, d = int(input()), {}                     #my 3 со словарем но надежней!))
# for i in [100,20,10,5,1]:
#     d[i] = n//i
#     n %= i
# print(sum(d.values()))
# print(d)

# print((n:=int(input())) % 1440 // 60, n % 60)          # Электронные часы
# print(*divmod(int(input()) % 1440, 60))

# print((n:=int(input())) + 2 - n % 2)

# n = int(input())
# часы = n//3600%24
# минуты = n%3600//60
# секунды = n%60
# print(f"{(n:=int(input()))//3600%24}:{n%3600//60:02}:{n%60:02}")          # Электронные часы 2

# n = float(input()); n *= 1.5; print(n)
# print(int(input())>0)
# print(not int(input())%6)
# print(bool(int(input())%9))
# print(int(input())%10==2)

# a, b = map(int, input().split())
# print(not a%7 and not b%7)

# a, b, c = map(int, input().split())
# print(len(set(map(int, input().split())))==1)
# print(5<int(input())<20)
# print(input()=='awesome' or 'awesome'==input())

# print(len(set(map(int, input().split()))) < 3)
# print(9<int(input())<100)

# ls = sorted(map(lambda x: int(x)**2, input().split()))
# print(ls[0]+ls[1]==ls[2])

# import math; print(math.ceil(int(input())/10))

# print(__import__('math').ceil(int(input())/4))

# print(sum([-(-int(input())//2) for i in 'oOo']))

# print(sum(map(__import__('math').ceil, [int(input())/2 for i in 'oOo'])))     # my 1.11.5

# l, w, h = map(int, input().split())
# print(-(-((l + w) * 2 * h) // 16))

print(hex(255))
print(type(hex(255)))