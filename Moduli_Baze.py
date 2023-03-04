import collections
import itertools
import random
import re
import math
import datetime


def get_max_count_word(counts_dict):
    max_count = 0
    max_count_word = None
    for word, count in counts_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word
    return max_count_word


def get_max_count_word_combinations(words, max_count_word):
    combinations = itertools.combinations(words, 2)
    max_count_word_combinations = [comb for comb in combinations if max_count_word in comb]
    # print(max_count_word_combinations)
    return max_count_word_combinations


def process(text):
    words = text.split(' ')
    print(words)
    counts = collections.Counter(words)
    print(counts)
    max_count_word = get_max_count_word(counts)
    print(max_count_word)
    max_count_word_combinations = get_max_count_word_combinations(words, max_count_word)
    random_combination = max_count_word_combinations[random.randint(0, len(max_count_word_combinations) - 1)]
    random_comb = random.choice(max_count_word_combinations)
    print(random_comb)
    return random_combination


text = "blue cat is parked right behind the blue building with blue walls and red door"
result = process(text)
print(result)
print("=" * 50)


res = math.sqrt(math.log(10, 2)) + math.exp(5) - (4 * math.pi)
print(res)
xxx = math.exp(8) + math.sqrt(17) + math.log(5)
print((xxx))
print("=" * 50)



def process_2(text):
    re_match = re.search('x=', text)
    equation = text[re_match.span()[1]:]
    print(equation)
    ops = {'exp': math.exp, 'sqrt': math.sqrt, 'log': math.log}
    actions = re.split(r"[+-]", equation)
    print(actions)
    result = 0
    for action in actions:
        action = action.replace('(', ' ').replace(')', '')
        print(action)
        op, value = action.split(' ')
        result += ops[op](int(value))
    print(result)
    report = "Result = {response} ; Date {date}."\
        .format(response=round(result, 3), date=datetime.datetime.now().strftime('%d.%m.%Y'))
    print(report)


t = "I want to be a professor, but only one thing I can solve is x=exp(8)+sqrt(17)+log(5)"
process_2(t)
