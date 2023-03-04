# def rec_count(index):       # макс.глубина рекурсии
#     print(index)
#     index += 1
#     rec_count(index)
#
# rec_count(1)

def values(n, current=1):  # вывод всех натуральных чисел от 1 до N
    if current <= n:
        print(current)
        values(n, current=current + 1)


# values(10)

def check_pow_2(n):  # является ли число степенью 2
    if n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print("NO")


# check_pow_2(1048576)

def sum_val(num, res=0):  # вычисляем сумму всех цифр десятичного числа
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)


# print(sum_val(234))

# 1. Напишите рекурсивную функцию, чтобы сгенерировать и вернуть список от 1 до N.
# Аргументом функции является только N.
# 2. Напишите функцию, которая рекурсивно ищет в сложном объекте значение. Сложный
# объект — это будет список списков списков и т.д. Например, [1, 2, [3, 4, [5, [6, []]]]]. Функция
# должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных
# игнорировать его.

def list1(n):
    return [char + 1 for char in range(n) if n >= 1]


print(list1(10))


def l_rec(n, index=1, x=[]):  # 1 задание. Генерация списка рекурсией
    if index <= n:
        x = x.append(index)
        return l_rec(n, index + 1)
    return x


print(l_rec(10))

data = [1, 2, [11, 22], 3, [4, 5, [6, 7, ["3", "5"], 8], 9]]


def print_list(x):  # 2 задание.
    for each_item in x:
        if isinstance(each_item, list):
            print(each_item)
            print_list(each_item)
        else:
            print(each_item)


print_list(data)


def serch1(dat, goal):  # 2 задание.
    for item in dat:
        if isinstance(item, list):
            print(item)
        return serch1(item, goal)

# serch1(data, [1])
