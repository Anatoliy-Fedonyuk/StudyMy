# def gets_nod(sex, sexy):
#     while sexy != 0:
#         sex, sexy = sexy, sex % sexy
#     return sex
#
# print(gets_nod(15, 121050))

# def get_rect_value(a, b, type=0): return a*b if type != 0 else (a+b)*2        # 7.4.2
# print(get_rect_value(4, 5, False))

# def check_password(st, chars="$%!?@#"): return len(st) > 7 and set(st)&set(chars) != set()      # 7.4.3
# print(check_password("12345678?"))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'q': 'q', 'w': 'w',
#      'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p', 'a': 'a',
#      's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'z': 'z',
#      'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', '!': '!'}
#
# def get_slug(st, sep="-"):      # 7.4.4
#     slug = ""
#     for s in st:
#         # print(t.get(s))
#         if s != " ":
#             slug += t.get(s)
#         else:
#             slug += sep
#     return slug
#
#
# sts = input().lower()
# print(get_slug(sts))
# print(get_slug(sts, sep="+"))

# def get_str_tag(st, tag="h1", up=True):
#     """Функция принимает на вход строку и заворачивает ее в указанный в параметре tag тег"""
#     tag = tag.lower() if up != True else tag.upper()
#     print(f"<{tag}>{st}</{tag}>")
#
# sts = input().strip()
# get_str_tag(sts, tag="div")
# get_str_tag(sts, tag="div", up=False)

# def get_even(*args): return [i for i in args if i%2 == 0]     # 7.5.3
# print(*get_even(45, 4, 8, 11, 12, 0))

# def get_biggest_city(*city): return max(city, key=len)
# print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))

# def get_data_fig(*args, **kwargs):      # 7.5.5 my
#     lst = [sum(args)]
#     lst.append(kwargs.get('type')) if 'type' in kwargs else None
#     lst.append(kwargs.get('color')) if 'color' in kwargs else None
#     lst.append(kwargs.get('closed')) if 'closed' in kwargs else None
#     lst.append(kwargs.get('width')) if 'width' in kwargs else None
#     return tuple(lst)


# def get_data_fig(*a, **k):              # 7.5.5 genius
#     return tuple([sum(a), *(k[i] for i in ('type', 'color', 'closed', 'width') if i in k.keys())])
#
# print(get_data_fig(5, 7, 8, 4, color=256, type=True, width=7, closed=False))

# def verify(ls):
#     for r in range(len(ls)-1):
#         for i in range(len(ls)-1):
#
#             if ls[r][i]+ls[r+1][i]+ls[r][i+1]+ls[r+1][i+1] > 1:
#                 return False
#
#     return True
#
# print(verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1]]))

# def str_min(st1, st2): return st1 if st1 < st2 else st2           # 7.5.6
# def str_min3(st1, st2, st3): return str_min(st3, str_min(st1, st2))
# def str_min4(st1, st2, st3, st4): return str_min3(st4, st3, str_min(st1, st2))

# x, *t, z = (1, 2, 3, 4, 5)
# print(t)
# print(x, z)

# *lst, x, y, z = map(int, input().split()); print(*lst)      # 7.6.2

# ls = input().split(); print((*ls,))

# a, b = map(int, input().split()); print(*range(a, b+1))     # 7.6.4

# print(*[*input().split(), *input().split()])          # 7.6.5

# import sys              # 7.6.6
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# menu = {**menu, **{i.split("=")[0]: i.split("=")[1] for i in lst_in}}
#
# print(dict(i.split('=') for i in lst_in))

# F = {                   # Тема Рекурсии!
#     'C:': {
#         'Python39': ['python.exe', 'python.ini'],
#         'Program Files': {
#             'Java': ['README.txt', 'Welcome.html', 'java.exe'],
#             'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
#         },
#         'Windows': {
#             'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
#         }
#     }
# }
#
#
# def get_files(path, depth=0):
#     for f in path:
#         print("     " * depth, f)
#         if type(path[f]) is dict:
#             get_files(path[f], depth + 1)
#         else:
#             print("     " * (depth + 1), " ".join(path[f]))
#
#
# get_files(F)


# def get_rec_N(N):       # 7.7.2
#     if N > 1:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(int(input()))

# def get_rec_sum(li): return li[0] if len(li) == 1 else li[0] + get_rec_sum(li[1:])
#
# print(get_rec_sum(list(map(int, input().split()))))

# N = int(input())          # 7.7.4
#
# def fib_rec(N, f=[1, 1]):
#     if len(f) != N:
#         f.append(f[-1] + f[-2])
#         fib_rec(N)
#     return f

# n = int(input())                        # 7.7.5
# def fact_rec(n): return n * fact_rec(n-1) if n >= 1 else 1

# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]    # 7.7.6

# def get_line_list(d, a=[]):
#     for i in d:
#         if type(i) == list:
#             get_line_list(i, a)
#         else:
#             a += [i]
#     return a

# def get_line_list(d, a=[]):
#     [a.append(i) if type(i) != list else get_line_list(i) for i in d]
#     return a

# N = int(input())          # 7.7.7

# def get_path(N): return N if N==1 or N==2 else get_path(N-1) + get_path(N-2)
# print(get_path(int(input())))

# -------------------------------------------------
# Сортировка слиянием
# -------------------------------------------------

# функция слияния двух отсортированных списков
# def merge_list(a, b):
#     c = []
#     N = len(a)
#     M = len(b)
#
#     i = 0
#     j = 0
#     while i < N and j < M:
#         if a[i] <= b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#
#     c += a[i:] + b[j:]
#     return c
#
# # функция деления списка и слияния списков в общий отсортированный список
# def split_and_merge_list(a):
#     N1 = len(a) // 2
#     a1 = a[:N1]     # деление массива на два примерно равной длины
#     a2 = a[N1:]
#
#     if len(a1) > 1: # если длина 1-го списка больше 1, то делим дальше
#         a1 = split_and_merge_list(a1)
#     if len(a2) > 1: # если длина 2-го списка больше 1, то делим дальше
#         a2 = split_and_merge_list(a2)
#
#     return merge_list(a1, a2)   # слияние двух отсортированных списков в один
#
#
# a = [9, 5, -3, 4, 7, 8, -8]
# a = split_and_merge_list(a)
#
# print(a)


# def merge_list(a, b):           # 7.7.9
#     c = []
#     N = len(a)
#     M = len(b)
#
#     i = 0
#     j = 0
#     while i < N and j < M:
#         if a[i] <= b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#
#     c += a[i:] + b[j:]
#     return c
#
# def split_and_merge_list(a):
#     N1 = len(a) // 2
#     a1 = a[:N1]
#     a2 = a[N1:]
#
#     if len(a1) > 1:
#         a1 = split_and_merge_list(a1)
#     if len(a2) > 1:
#         a2 = split_and_merge_list(a2)
#
#     return merge_list(a1, a2)
#
# ls = [*map(int, input().split())]
# print(*split_and_merge_list(ls))

# get_sq = lambda x: x**2

# get_div = lambda a, b: a/b if b != 0 else None

# print((lambda x: abs(x))(float(input())))

# print((lambda s: "ra" in s)(input()))       # 7.8.5

# def filter_lst(it, key=None):      # 7.8.6
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
# ls = [*map(int, input().split())]
# ll = [None, lambda x: x < 0, lambda x: x >= 0, lambda x: 2 < x < 6]
# [print(*filter_lst(ls, key=l)) for l in ll]

# filter_lst = lambda it, key=None: tuple(it if key is None else filter(key, it))     #  7.8.6 var
#
# ls = [*map(int, input().split())]
# ll = [None, lambda x: x < 0, lambda x: x >= 0, lambda x: 2 < x < 6]
# [print(*filter_lst(ls, key=l)) for l in ll]

# a = lambda *x: sum(list(*x))
# print(a([2, 5, -3, 9, 0, -11, 22]))

# WIDTH = int(input())
#
#
# def func1():
#     global WIDTH
#     WIDTH += 1
#     return WIDTH
#
#
# print(func1())

# def func1():
#     msg = input()
#
#
#     def func2():
#         nonlocal msg
#         msg = input()
#         print(msg)
#
#
#     func2()
#     print(msg)
#
#
# func1()


# def strip_string(strip_chars=' '):          # Замыкания!!!!!! спаршивают на собеседованиях
#     def do_strip(string):
#         return string.strip(strip_chars)
#
#     return do_strip
#
#
# # strip1 = strip_string()
# # strip2 = strip_string(" !?,.;")
# #
# # print(strip2(" ?hello python!...;   "))
# print(strip_string(" ;?")(" ?hello python!...;   "))  # Оч.интересно вторые скобки это арг.уже сразу для вложенной функции!

# def counter_add(n):             # 7.10.2 7.10.1
#     def add(number):
#         return number + n
#
#     return add
#
#
# cnt = counter_add(2)
# print(cnt(int(input())))
# cnt2 = counter_add(12)
# print(cnt2(7))


# def make_tag(tag):              # 7.10.4 7.10.3
#     def str_tag(s):
#         return f"<{tag}>{s}</{tag}>"
#
#     return str_tag
#
# tag_name, string = input(), input()
# str1 = make_tag(tag_name)
# print(str1(string))

# def get_collection(tp):              # 7.10.5
#     def inner(coll):
#         return tuple(coll) if tp != 'list' else list(coll)
#
#     return inner
#
# tp, coll = input(), map(int, input().split())
# lst = get_collection(tp)(coll)
# print(lst)

# def func_show(func):          # 7.11.1
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Площадь прямоугольника: {result}")
#         return result
#     return wrapper
#
#
# def get_sq(width, height): return width * height


# def show_menu(func):              # 7.11.2
#     def inner(*args):
#         [print(f"{i}. {item}") for i, item in enumerate(func(*args), start=1)]
#     return inner
#
#
# @show_menu
# def get_menu(s): return s.strip().split()
#

# st = input()
# get_menu(st)


# def sorted_list(func):              # 7.11.3
#     def inner(*args):
#         return sorted(func(*args))
#     return inner
#
#
# @sorted_list
# def get_list(st):
#     return [int(i) for i in st.split()]
#
# s = input()
# print(*get_list(s))


# def get_dict(func):             # 7.11.4
#     def inner(*args):
#         return dict(zip(*func(*args)))
#     return inner
#
#
# @get_dict
# def get_list(s1, s2):
#     return s1.split(), s2.split()
#
#
# d = get_list(input(), input())
# print(*sorted(d.items()))

# Преобразование в слаг               # 7.11.5 my
# ---------------------------------------------
# def rem_space(f):
#     def inner(*args):
#         str = f(*args)
#         while "--" in str:
#             str = str.replace("--", "-")
#         return str
#     return inner
#
# @rem_space
# def get_latin(st):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
#          ' ': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}
#     for _ in st:
#         if _ in t:
#             st = st.replace(_, t[_])
#     return st
#
# print(get_latin(input().lower()))


# Преобразование в слаг               # 7.11.5 расширенная версия
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def rem_space(func): return lambda *args: '-'.join(func(*args).replace('-', ' ').split())
#
# @rem_space
# def get_latin(st: str): return ''.join(t.get(x, x) if x not in ":;., _" else '-' for x in st)
#
# print(get_latin(input().lower()))


# def param_decor(start):             # 7.12.1 Декораторы с параметрами
#     def real_decor(func):
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs) + start
#         return wrapper
#     return real_decor
#
#
# @param_decor(5)
# def get_list_sum(s):
#     return sum([*map(int, s.split())])
#
#
# # get_list_sum = param_decor(5)(get_list_sum)
# print(get_list_sum(input()))

# def make_tag(tag="h1"):              # 7.12.2
#     def str_tag(func):
#         def wrapper(*args):
#             return f"<{tag}>{func(*args)}</{tag}>"
#         return wrapper
#     return str_tag
#
#
# @make_tag("div")
# def str_low(string):
#     return string.lower()
#
#
# print(str_low(input()))

# from functools import wraps              # 7.12.3
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def dekor_str(chars=" !?"):
#     def rem_space(func):
#         @wraps(func)
#         def wrapper(*args):
#             res = ''.join(x if x not in chars else '-' for x in func(*args))
#             return res.replace('---', '-').replace('--', '-')
#         return wrapper
#     return rem_space
#
# @dekor_str(chars="?!:;,. ")
# def get_latin(st: str):
#     return ''.join(t.get(x, x) for x in st.lower())
#
# print(get_latin(input()))


from functools import wraps

def param_decor():             # 7.12.4 Декораторы с параметрами
    def real_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return sum(func(*args, **kwargs))
        return wrapper
    return real_decor


@param_decor()
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return [*map(int, s.split())]

print(get_list(input()))