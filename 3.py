# ------------------------------ # 1 # ------------------------------ #

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def a_1(num_1, num_2):
    return num_1 / num_2

num_1 = int(input('Enter dividend: '))
num_2 = int(input('Enter divider: '))
try:
    int(num_1 / num_2)
except ZeroDivisionError:
    print("You can't divide by zero")

print(int(a_1(num_1, num_2)))

# ------------------------------ # 2 # ------------------------------ #

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# ----------------------------------- # 1.1 # ---------------------------------

# def user(name=input('Name: '), surname=input('Surname: '), birthday=int(input('Year of birth: ')), city=input('Сity of residence: '), email=input('Your email: '), tel=int(input('Your phone number: '))):
#     print(f'User {name} {surname},born in {birthday}, lives in {city}, email: {email}, phone number: {tel}.')
# user()

# ----------------------------------- # 1.2 # ---------------------------------


# def user(name, surname, **data_user):
#     print(f'User {name} {surname}')
#     for data, user in data_user.items():
#         print(f'{data}, {user}')
# user(
#     input('Name: '),
#     input('Surname: '),
#     birthday=int(input('Year of birth: ')),
#     city=input('Сity of residence: '),
#     email=input('Your email: '),
#     tel=int(input('Your phone number: ')),
# )

# ----------------------------------- # 1.3 # ---------------------------------

def user(name='Иван', surname='Пупкин', birthday=1999, city='Воронеж', email='PupkinIvan@mil.ru', tel='987654321'):
    print(f'User {name} {surname},born in {birthday}, lives in {city}, email: {email}, phone number: {tel}.')
user()

# ------------------------------ # 3 # ------------------------------ #

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 < arg_2:
        if arg_2 < arg_3:
            print(arg_2 + arg_3)
        else:
            print(arg_2 + arg_3)
    else:
        if arg_2 > arg_3:
            print(arg_1 + arg_2)
        else:
            print(arg_1 + arg_3)

my_func(
        arg_1=int(input("Enter 1: ")),
        arg_2=int(input("Enter 2: ")),
        arg_3=int(input("Enter 3: "))
    )

# ------------------------------ # 4 # ------------------------------ #

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def multiplication(x, y):
    z = -1
    x1 = x
    while z > y:
        x = x1 * x
        z -= 1
    print(1 / x)

multiplication(
    x=int(input('Enter a positive number: ')),
    y=int(input('Enter a negative number: '))
    )

# ------------------------------ # 5 # ------------------------------ #

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

#
#     li = []
#     b = False
#     s = 0
#     while b != True:
#         li = input('Enter number: ').split(' ')
#         for item in li:
#             if item != 'end':
#                 s += int(item)
#             else:
#                 b = True
#         print(s)
#

finish = False
summa = 0

def fplus(**kwargs):
    global finish, summa
    for item in kwargs['li']:
        if item != kwargs['endKey']:
            summa += int(item)
        else:
            finish = True
            break


while finish != True:
    fplus(li=input('Enter number: ').split(' '), endKey='end')
    print(summa)

# ------------------------------ # 6 # ------------------------------ #

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# i = 0
# def letters():
#     global i
#     for i in range(len(word)):
#         if i == word.lower[0]:
#
#     return word.upper[0]
# word = str(input('Word: '))
# print(letters())

# letters()

def letters(word):
    return word.title()

s = ''

source = input('Words: ').split()
for word in source:
    s += letters(word) + ' '

print(s)

# ------------------------------ #   # ------------------------------ #
