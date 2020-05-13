# ------------------------------ # 1 # ------------------------------ #

# 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("file.txt", "w", encoding='utf-8') as file:
    [file.write(input('Write something: ') + '\n') for line in range(10)]

# ------------------------------ # 2 # ------------------------------ #

# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


lines = 0
f = open("file.txt")
for line in f:
    lines += 1
    print(f'{lines})  {len(line.split(" "))} слов(а) в строке')
print(f'Всего строк {lines}')

# ------------------------------ # 3 # ------------------------------ #

# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("text_3.txt", mode="r", encoding="utf-8") as text:
    sum = 0
    c = 0
    for lines in text:
        line = lines.split(' ')
        d = float(line[1])
        if d <= 20000:
            sum += d
            c += 1
            print(line[0])

print(f'общая зарплата = {sum}\nколиество сотрудников = {c}\nсредняя зарплата = {sum / c}')

# ------------------------------ # 4 # ------------------------------ #

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


import requests
import json

def translite(mytext):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    header = {
        'key': 'trnsl.1.1.20200430T082733Z.85b6612657c93ee8.585c0f93bcee04107113a975a6e01876481a2ede',
        'lang': 'en-ru',
        # 'hint': 'en, ru',
        'text': mytext,
    }
    data = {}
    try:
        r = requests.get(url, params=header)
        data = r.json()
        with open('response.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except:
        print('Ошибка получения данных.')
    return data

l = []
ll = []
with open('text_4.txt', 'r') as file:
    for line in file.readlines():
        l.append(line.split(' - ')[0])
        ll.append(line.split(' - ')[1])
with open('text_4.1.txt', 'w') as file:
    data = translite(l)
    if data != {}:
        l = data['text']
        for i in range(len(l)):
            file.write(l[i] + ' - ' + ll[i])
    else:
        print('Ошибка в сервисе yandex translate')

# ------------------------------ # 5 # ------------------------------ #

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import numpy
a = numpy.random.randint(1, 20, 15)

with open('text_5.txt', 'w', encoding='utf-8') as text:
    for d in a:
        text.write(str(d) + ' ')
with open('text_5.txt', 'r', encoding='utf-8') as text:
    l = text.readline().split(' ')
    # print(l)
    sum = 0
    for i in range(len(l)-1):
        sum += int(l[i])

    print(sum)

# ------------------------------ # 6 # ------------------------------ #

# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

les = []

with open('text_6.txt', 'r', encoding='utf-8') as lessons:
    for lession in lessons.readlines():
        l = lession.split(':')
        name = l[0]
        pp = l[1].split(' ')
        itog = 0
        for p in pp:
            if p not in ['', '-', '-\n']:
                p = p.split('\n')[0]
                lections_count = '0'
                labs_count = '0'
                practics_count = '0'
                if p.count('л)'):
                    lections_count = p.split('(')[0]
                elif p.count('лаб)'):
                    labs_count = p.split('(')[0]
                elif p.count('пр)'):
                    practics_count = p.split('(')[0]
                itog += int(lections_count) + int(labs_count) + int(practics_count)
        les = {name, itog}
        print(les)

# ------------------------------ #   # ------------------------------ #
