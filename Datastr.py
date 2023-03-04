user = {
    "name": "JohnDoe",
    "info": {"basic": {"age": 25, "salary": 5000},
             "additional": {"study": "mathematics", "family": "married"},
             "special": {"projects": [
                 {"name": "quantum_computer", "stage": "in_progress"},
                 {"name": "laser_gun", "stage": "in_production"}
             ]
             }
             }
}

# print(user)

# def get_data(data_dict, keys):    # метод обращения к сложным данным
#     data = data_dict
#     for key in keys:
#         data = data[key]
#     return data
#
# print(get_data(user, ["info", "additional"]))
# print(get_data(user, ["info", "basic", "age"]))
# print(get_data(user, ["info", "special", "projects", 0, "stage"]))
# print(get_data(user, ["info", "special", "projects", 1]))

def get_data_rec(data_dict, keys, index=0):    # метод обращения к сложным данным - рекурсией
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index+1)
    return data_dict

print("=" * 30)
print(get_data_rec(user, ["info", "additional"]))
print(get_data_rec(user, ["info", "basic", "age"]))
print(get_data_rec(user, ["info", "special", "projects", 0, "stage"]))
print(get_data_rec(user, ["info", "special", "projects", 1]))


# 1. Напишите комбинацию циклов чтобы проитерировать все элементы сложной структуры
# данных вида d = {“a”: {“1”: [...], “2”: [...], ...}, ...} (словарь словарей в которых лежат списки)
# 2. Напишите comprehension, который итерирует строку “1_2,40_5,5_32” (разбить по запятым)
# и каждый элемент разбивает по символу “_” и полученные элементы приводит к типу int,
# и складывает их, тем самым образуя список целых чисел. (Вы можете использовать lambda
# функцию или написать обычную, которая принимает строку вида “1_2” на вход и
# возвращает число как сумму значений из строки; используйте метод split())

