'''Инди-курс по Python'''

# print(a:='Я стану крутым программистом!', a, a, sep='\n')
# print('W'*777)
# print('Лев Николаевич Толстой написал "Война и мир"')
# print(input(), input(), sep='\n')

# s = [input() for _ in '___'][::-1]

# [print(x) for x in [input() for _ in '___'][::-1]]

# print(f"{(a:=input())} {a} {a} {a}")

# print(len(input()))
# print("{1}{0}".format(input(), input()))
# print(input()*3)

# a,b,c = input().split()

# [print(f"Simvol code {x} is {ord(x)}.") for x in input().split()]

# s = input()
# print((s:=input())[-1] + s[:-1])

# print(input().lower())

# print(input().upper()==input().upper())

# print(''.join([(s:=input())[:3].upper(), s[3:-3].lower(), s[-3:].upper()]))

# print(input().title().swapcase())

# print(input().lower().count('e'))

# print(input().rfind('a'))
# print(input().replace(' ',','))
# print(input().replace('w','').replace('z',''))

# print(''.join([s for s in input().lower() if s not in "aoyeui"]).replace('','.')[:-1])

# print(len(input().split()))

# print('-'.join(['Follow', 'the', 'Cops', 'Back', 'Home']))
# print(input().lower().startswith("mam"))

# print(input().endswith(input()))
# print((s:=input()).startswith(input()) and s.endswith(input()))

# print(input().isdigit())
# print(input().isupper())
# print(input().islower())

# print(input().ljust(15, "-"))
# print(input().rjust(10, "!"))
# print(input().center(15, "_"))
# print(input().zfill(10))

# print(input().strip('-_!?'))
# print(input().rstrip('-_!?'))

# def get_RGB(r: str, g: str, b: str) -> str:
# ls = [hex(int(input()))[2:].zfill(2) for _ in '0o0']
# print(F"#{''.join(ls).upper()}")

# print("/\_/\ \n>^,^< \n / \ \n(|_|)_/")
# print(r'''
#   /~~~\
#  //^ ^\\
# (/(_*_)\)
# _/''*''\_
# (/_)^(_\)
# ''')

# a = 255
# print(F'#{a:05X}')

# print("Что Вы сказали? {}? Какое интересное слово".format(input()))

# print("Здравствуйте, {1} {0}!".format(input(), input()))

# print('Для числа {} предыдущим будет число {}.'.format((x:=input()), (int(x)-1)))
# print('Для числа {} следующим будет число {}.'.format(x, (int(x)+1)))

# print(f"Мое имя {input()}!")
# print(f"Hello {input().upper()}. You are {input()} years old.")
# print(f"{input()}, вам исполнится 77 лет в {int(input())+77}")
# print("{} сек - это {} мин. {} сек.".format((s:=input()), int(s)//60, int(s)%60))

# w, h = map(int, input().split())
# print(f"Разрешение экрана: {w} x {h}.\nОбщее количество пикселей = {w*h}.")

# print(f"{(d:=int(input()))} / {(f:=int(input()))} = {d/f}\n{d} // {f} = {d//f}\n{d} % {f} = {d%f}")

# x, y, z = (int(input()) for _ in "xyz")
# print(f"Vector A({x}, {y}, {z})\nVector B({x+5}, {y+5}, {z+5})")

# print(f"""Current dollar rate is {(r:=input())}. You want to buy {(d:=input())} dollars
# You must pay {int(d)*float(r)}""")

# x, y = int(input()), int(input())
# print(f"Точка({x = }, {y = })")
# print(f"{(float(input())):.2f}")

# print(f'Число\tКвадрат\t  Куб')
# for x in range(1, 11):
#    print(f'{x:03}\t\t{x*x:03}\t\t{x*x*x:04}')
# print(f"{(int(input())):010}")

### НАСТОЯЩИЙ ЧЕК!!!!!
# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_cheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

# print(f"|{int(input()):-^15}|")

# text = input()
# print(f"|{text:&^20s}|")
# print(f"|{text:&>20s}|")
# print(f"|{text:&<20s}|")

# print(my_list:=[1]*77)
# print(my_list:=['q', 'w', 't']*15)
# print('777' in input().split())
# print(sum([*map(int, input().split())]))
# print(min(l:=[*map(int, input().split())]), max(l))
# print(sum(l:=[*map(int, input().split())])/len(l))
# print([*map(int, input().split())][::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# match top:
#     case t if 'Бригада' in t: top[t.index('Бригада')] = "Сверхъестественное"
# match top:
#     case t if 'Друзья' in t: top[t.index('Друзья')] = "Настоящий детектив"
# print(top)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# match int(input()):
#     case m if 0 < m < 13: print(months[m-1])
#     case _: print("Incorrect input")

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# [numbers.append(e) for e in [111, 222, 789, 201]]
# print(numbers)

# num = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# [num.insert(i, v) for i, v in {5: 111, 8: 222, 0: 789, 11: 201}.items()]; print(num)

# num = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# # num.extend([43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]); print(num)
# s = 0
# for i in [-1, 0, 12, 7]:
#     s += num.pop(i)
# print(num, s, sep="\n")

# num = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# [num.remove(i) for i in (3,5,7,9)]; print(num)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True); print(numbers)

# a = [*map(int, input().split())]
# print(list(reversed([*map(int, input().split())])))

# l = [*map(int, input().split())]
# print([*map(int, input().split())].count(999))

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# copy_numbers = numbers[:]; print(copy_numbers)

# print(*map("-".join, input().upper().split()))
# re = input().upper()
# print('-'.join(re).replace('- -',' '))

# fio = input().split()
# print(f"{fio[2]} {fio[0][0]}.{fio[1][0]}.")
# print('{2} {0[0]}.{1[0]}.'.format(*input().split()))

# s = "\n".join(input().split())
# print("\n".join(input().split()))

# a = input().split()
# print('''
# '''.join(a))

### MODULE RE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import re

# text = "lat = 5, lon=7, a=5"
# print(re.findall(r"(lat|lon)\s*=\s*(\d+)", text))

# text = "Картинка <img src='bg.jpg'> в тексте</p>"
# print(re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text))
# print(re.findall(r"<img\s+[^>]*src=(?P<quote>[\"'])(.+?)(?P=quote)", text))
# print(re.findall(r"<img\s+[^>]*(src=(?P<quote>[\"']).+?)(?P=quote)", text))

# with open("map.xml", "r") as f:
#     lat = []
#     lon = []
#     for text in f:
#         match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[0-9.,]+)\1",
#                           text)
#         if match:
#             v = match.groupdict()
#             print(v)
#             if "lon" in v and "lat" in v:
#                 lon.append(v["lon"])
#                 lat.append(v["lat"])
#
#     print(lon, lat, sep="\n")

# text = """<!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Уроки по Python</title>
# </head>
# <body>
# <p align=center>Hello World!</p>
# </body>
# </html>"""
#
# # print(re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE))     #тут корректней так как съедает пробел перед кавычками
# # print(re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"'](.+?)[\"'](?<![ \t])", text, re.MULTILINE))
#
# match = re.findall(r"""([-\w]+)             #выделяем атрибут
#                    [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
#                    (?P<q>[\"'])?            #проверяем наличие кавычки
#                    (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение r в зависимости от того были ли кавычки
#                    """,
#                    text, re.MULTILINE|re.VERBOSE)
# print(match)

# text = "Python, python, PYTHON"
# match = re.findall(r"(?im)python", text)
# print(match)

# s = input()
# print(d if (d:=int(input()))<20000 else d*0.87)

# a, b = int(input()), int(input())
# print((a, b)[b > a])

# a, b, c = map(int, input().split())
# print(('YNEOS')[(a+b!=c)::2])

# a = input().split()
# print([int(i) for i in input().split() if i not in '3579'])

# match (s:=int(input())):
#     case s if s < 10001: print(f'Сумма {s} не превышает лимит, проходите')
#     case _: print(f'Ого! {s}! Куда вам столько? Мы заберем {s-10000}')

# match (st:=input()):
#     case s if 'walrus' in s: print('Нашли моржа')
#     case _: print('Никаких моржей тут нет')

# print(('YNEOS')[((s:=input())[::-1]!=(t:=input()))::2])

# print(('YNEOS')[((N:=input())[::-1]!=N)::2])

# match [int(input()) for i in '0_0']:
#     case a, b, c if (a+b)>c and (b+c)>a and (a+c)>b: print('YES')
#     case _: print('NO')

# N = list(map(int, input()))                       #3.1.14 my
# [N.insert(0,0) for x in (6-len(N))*'_']
# print(('YNEOS')[sum(N[:3])!=sum(N[3:])::2])

# n = [int(i) for i in input()]
# print(('NO', 'YES')[sum(n[:-3])==sum(n[-3:])])

# # n = [*map(int, input().zfill(6))]
# # print(n)
# print(('YNEOS')[sum((n:=[*map(int, input().zfill(6))])[:3])!=sum(n[3:])::2])                      #3.1.14 my

# l, a, b = '_abcdefgh', input(), input()
# a_col = 'black' if not (int(a[1])+l.index(a[0])) % 2 else 'white'
# b_col = 'black' if not (int(b[1])+l.index(b[0])) % 2 else 'white'
# print(("YES","NO")[a_col != b_col])

l, a, b = '_abcdefgh', input(), input()                                 #3.1.15 my
print(("YES","NO")[(int(a[1])+l.index(a[0])+int(b[1])+l.index(b[0]))%2])