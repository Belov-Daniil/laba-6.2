# . У няни 7 разных фруктов (ф1,…ф7).
# Сформировать (вывести) все возможные варианты меню полдника
# (1 фрукт) для ребенка на неделю.
# Доп. условие
# киви должно стоять в неделе раньше яблока а ананас позже
from itertools import *
import numpy as np

fruit_basket = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']

all_variants = []


def iter():
    for i in permutations(fruit_basket, 7):
        all_variants.append(i)
    return all_variants


def rec(a, k):
    if k == 1:
        return [[x] for x in a]
    else:
        return [[x] + y for x in a for y in rec(a, k - 1)]


def start():
    print(
        'У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.')
    a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    while a != 'rec' and a != 'iter':
        a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    if a == 'rec':
        print(
            'В качестве усложнения составления расписания напишите три фрукта из представленных на выбор:'
            ' apple, pineapple, orange, banana, pear, kiwi, avocado'
            ' Они будут стоять в меню таким обазом - Фрукт 1 будет всегда до фрукта 2, а фрукт 3 будет после фрукта 2')
        fruits_name = input().split(' ')
        while len(fruits_name) < 3 or fruits_name[1] not in fruit_basket or fruits_name[0] \
                not in fruit_basket or fruits_name[2] not in fruit_basket:
            fruits_name = input(' напишите три фрукта из представленных на выбор: apple, pineapple,'
                                ' orange, banana, pear, kiwi, avocado\n').split(' ')
        p = 0
        fr = rec(fruit_basket, 7)
        for j in fr:
            if len(np.unique(j)) < 7:
                pass
            else:
                if not (j.index(fruits_name[0]) < j.index(fruits_name[1])  > j.index(fruits_name[2])):
                    pass
                else:
                    p += 1
                    print(*j)
        print('общее кол-во вариантов меню на неделю : ' + str(p))
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()
    else:
        print(
            'В качестве усложнения составления расписания напишите три фрукта из представленных на выбор:'
            ' apple, pineapple, orange, banana, pear, kiwi, avocado'
            ' Они будут стоять в меню таким обазом - Фрукт 1 будет всегда до фрукта 2, а фрукт 3 будет после фрукта 2')
        fruits_name = input().split(' ')
        while len(fruits_name) < 3 or fruits_name[1] not in fruit_basket or fruits_name[0] \
                not in fruit_basket or fruits_name[2] not in fruit_basket:
            fruits_name = input(' напишите три фрукта из представленных на выбор: apple, pineapple,'
                                ' orange, banana, pear, kiwi, avocado\n').split(' ')
        p = 0
        fi = iter()
        for j in fi:
            if not (j.index(fruits_name[0]) < j.index(fruits_name[1]) < j.index(fruits_name[2])):
                continue
            else:
                print(j.index(fruits_name[0]) < j.index(fruits_name[1]) < j.index(fruits_name[2]))
                p += 1
                print(*j)
        print('общее кол-во вариантов меню на неделю : ' + str(p))
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()


start()
