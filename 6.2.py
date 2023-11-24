#. У няни 7 разных фруктов (ф1,…ф7).
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
    print('У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.')
    print('Спустя некоторое время няня поняла что если поставить в распивании киви после яблока а ананас до то у ребёнка несварение. Поэтому  ')
    print('киви должно стоять в неделе раньше яблока а ананас после')
    a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    while a != 'rec' and a != 'iter':
        a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    if a == 'rec':
        p = 0
        fr = rec(fruit_basket, 7)
        for j in fr:
            if len(np.unique(j)) < 7:
                pass
            else:
                if j.index('kiwi') < j.index('apple') > j.index('pineapple'):
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
        p = 0
        fi = iter()
        for j in fi:
            if j.index('kiwi') < j.index('apple') > j.index('pineapple'):
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

start()
