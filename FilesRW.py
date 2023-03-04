# import random
# import datetime

import json
import csv
from xml.dom import minidom
from xml.etree import ElementTree

# try:
#     with open("Dzen.txt", 'r', encoding='utf-8') as f:
#         s = f.read()
#         # d = f.readlines()
#         print(s)
#         # print(d)
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# except:
#     print('Ошибка при работе с файлом')
# finally:
#     print(f.closed)

# try:
#     with open("save.txt", 'a+') as file:
#         file.seek(0)
#         file.writelines(["Hallo 4\n", "Hallo 5\n"])
#         s = file.readlines()
#         print(s)
#         # file.write("Hallo 2\n")
#         # file.write("Hallo 3\n")
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# except Exception:
#     print('Ошибки при работе с файлами')

# filename = 'my_file.json'
# with open(filename, 'r', encoding='utf-8') as file:
#     data = json.load(file)
# print(data)
# data.append({"name": "Artur", "age": 11})
# print(data)
# with open("my_file2.json", 'w', encoding='utf-8') as file:
#     json.dump(data, file)


# my_doc = minidom.parse('my_file.xml')
# items = my_doc.getElementsByTagName("item")
# print(items)

# with open("data.csv", 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     data = [row for row in csv_reader]
#
#     print(data)
# data.append(["Mike", "35", "male"])
# print(data)
# with open("data.csv", "w") as data_file:
#     csv_writer = csv.writer(data_file, delimiter=",")
#     for row in data:
#         csv_writer.writerow(row)

# letters = "abcdefghijklmnopqrstuvwxyz"
# # print(len(letters))
# random_latters = ""
# random_count = 25
# while len(random_latters) < random_count:
#     random_latter = letters[random.randint(0, len(letters)-1)]
#     random_latters += random_latter
#
# print(random_latters)
# with open('random_string', 'w') as text_file:
#     text_file.write(random_latters)

# users = ['Artur', 'Kate', 'Alice', 'Mike', 'Nike']
# users_list = []
# for user in users:  # Создаем список словарей
#     users_list.append({'name': user, 'age': random.randint(1,99)})
# print(users_list)
# data = {'data': users_list,
#         'current_date': datetime.datetime.now().strftime('%d.%M.%Y')}
# print(data)
# filename = "users_data_{current_date}.json".format(current_date = data["current_date"])
# with open(filename, 'w') as json_file:
#     json.dump(data, json_file)

# with open('users_data_17.12.2022.json', 'r') as file:
#     data = json.load(file)
# print(data)
# rows = []
# for user in data['data']:
#     rows.append(list(user.values()))
# rows = [list(data['data'][0].keys())] + rows
# print(rows)
# with open("users_data_{date}.csv".format(date=data['current_date']), 'w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for row in rows:
#         csv_writer.writerow(row)

# with open('users_data_17.12.2022.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=',')
#     data = [row for row in reader]
#
# columns = data[0]
# users = data[1:]
# print(columns)
# print(users)
#
# xml_data = ElementTree.Element('data')
# items_holder = ElementTree.SubElement(xml_data, 'users')
# items = [ElementTree.SubElement(items_holder, 'user') for i in range(len(users))]
#
# for j in range(len(users)):
#     item = items[j]
#     for k in range(len(columns)):
#         item.set(columns[k], users[j][k])
# xml_file = ElementTree.tostring(xml_data)
# with open('users.xml', 'wb') as file:
#     file.write(xml_file)





# absolute = 'C:\\Users\\HP\\Desktop\\Project_X\\courses\\doc\\random_string'
# relative = 'courses/doc/random_string'
# with open('random_string', 'r') as file:
#     print(file.read())



# 1. Скачайте таблицу данных в виде csv файла по ссылке.
# 2. Прочитайте файл и преобразуйте его в список словарей, где ключами будут имена
# колонок, а значения — это данные из списков.
# 3. Сохраните полученный список словарей в JSON файл.
# 4. По аналогии с примером 4 на уроке, сделайте свой автоматический генератор XML, где
# вместо юзеров будут данные о людях в полученном вами JSON файле. Сохраните
# полученный XML.

# with open('titanic.csv', 'r', encoding='UTF-8') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     data = [row for row in csv_reader]
# print(data)

# data = [['name', 'age', 'gender'], ['Artur', '13', 'male'], ['Kate', '39', 'female'],
#         ['Alice', '67', 'female'], ['Mike', '90', 'male'], ['Nike', '66', 'male'], ['Lilu', '23', 'female']]
#
# columns = data[0]
# passeng = data[1:]

# lst = []      # Запасной вариант))
# for i in range(len(passeng)):
#     d = dict(zip(columns, passeng[i]))
#     # print(d)
#     lst.append(d)
# print(lst)

# titan = []
# for i in range(len(passeng)):
#     sps = {}
#     for j in range(len(columns)):
#         sps.update({columns[j]: passeng[i][j]})
#     # print(sps)
#     titan.append(sps)
# print(titan)
#
# with open('titanic.json', 'w', encoding='UTF-8') as json_file:
#     json.dump(titan, json_file)





# with open('titanic.csv', 'r', encoding='UTF-8') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     data = [row for row in csv_reader]
# # print(data)
#
# columns = data[0]
# passengers = data[1:]
# # print(passengers)
# # print(columns)
#
# xml_data = ElementTree.Element('data')
# items_holder = ElementTree.SubElement(xml_data, 'passengers')
# items = [ElementTree.SubElement(items_holder, 'passenger') for i in range(len(passengers))]
#
#
# for j in range(len(passengers)):
#     item = items[j]
#     for k in range(len(columns)):
#         item.set(columns[k], passengers[j][k])
#
#
# xml_file = ElementTree.tostring(xml_data)
# with open('titanic.xml', 'wb') as file:
#     file.write(xml_file)
