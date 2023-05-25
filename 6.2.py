fruits = ['Груша - 300 калорий', 'Банан - 400 каллорий', 'Яблоко - 150 калорий', 'Персик - 465 калорий', 
          'Манго - 450 калорий', 'Гранат - 250 калорий', 'Апельсин - 333 калорий']

days = ['Понедельник', 'Вторник', 'Среда',
        'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

fruits_list = []

for a in fruits:
    for b in fruits:
        if a != b:
            for c in fruits:
                if c not in (a, b):
                    for d in fruits:
                        if d not in (a, b, c):
                            for e in fruits:
                                if e not in (a, b, c, d):
                                    for f in fruits:
                                        if f not in (a, b, c, d, e):
                                            for g in fruits:
                                                if g not in (a, b, c, d, e, f):
                                                    fruits_list.append((a, b, c, d, e, f, g))

count = 0
for j in range(0, len(fruits_list)):
    for i in range(0, 7):
        s = days[i] + ": " + str(fruits_list[j][i])
        print(s)
    print()
    count += 1

print('Возможных расстановок 7 фруктов по дням недели - ' + str(count))