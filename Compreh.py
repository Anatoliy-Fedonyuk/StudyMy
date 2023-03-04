# Comprehensions
#
# chars = [char.upper() for char in "included" if char != "d"]
# print(chars)
#
# names = ['mike', 'john', 'sally']
# names = [name.capitalize() for name in names]
# print(names)
#
# even = [num ** 2 for num in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} if num % 2 != 0]
# print(even)
#
# puw = [vol // 2 for vol in range(10, 0, -1)]
# print(puw)
#
# w1 = {v ** 3 for v in [1, 3, 5, 5, 2, 1, 7, 3]}
# print(w1)

data = ['john_25', 'sally_19', 'susan_45', 'jack_16']
data_new = {(x.split('_')[0]).capitalize(): int(x.split('_')[1]) for x in data}
print(data_new)

# months = tuple(num + 1 for num in range(12))
# print(months)
#
# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)
#
# flatten_matrix = [val for sublist in matrix for val in sublist]
# print(flatten_matrix)

#  Задачи: создание списка словарей и последующее уплощение до списка распакованных списков
def func(index, count):
    return {"ID": index, "values": ["{}_{}".format(index, value) for value in range(count)]}


print(func(1, 5))

def generate(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]

r = generate(10)
print(r)
final = [value for sublist in r for value in sublist["values"]]
print(final)

print({v+2: v for v in range(10)})
