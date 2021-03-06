# -----------------------------------# 1 # -----------------------------------#

# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# выполнено 15.04.2020

a = 10
print(a)

b = 'world'
print(b)

c = 2.1
print(c)

d = True
print('Тип данных ', type(d))

e = str(input('enter something: '))
print(type(e))

f = [1, 'and', 2, 4.5, 'hello']
print('Тип данных ', type(f))

g = {'one', 2, 3.1}
print(g)

h = (0, 1.2, 'two')
print(h)

i = int(input('enter something number: '))
print('Тип данных ', type(i))

# -----------------------------------# 2 # -----------------------------------#

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# выполнено 15.04.2020

t = int(input('Ведите время в секундах: '))

h = t // 3600
m = (t // 60) % 60
s = (t % 3600) % 60

if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)

print(f'Время: {h}:{m}:{s}')

# -----------------------------------# 3 # -----------------------------------#

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# выполнено 15.04.2020


# n_0 = int(input('Введите число: '))  // первый вариант
# n_1 = str(n_0) * 2
# n_2 = str(n_0) * 3
# r = n_0 + int(n_1) + int(n_2)
# print(r)

# // второй вариант:

n_0 = int(input('Введите число: '))
n_1 = n_0 * 10 + n_0
n_2 = n_1 * 10 + n_0
r = n_0 + n_1 + n_2
print(r)

n_0 = int(input('Введите число: '))
n_1 = n_0 ** 10
print(n_1)

# -----------------------------------# 4 # -----------------------------------#

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# выполнено 15.04.2020

n = int(input('Введите число: '))
d = n % 10
g = n // 10
while g > 0:
    g = g // 10
    d1 = g % 10
    if (d < d1):
        d = d1

print(d)

# -----------------------------------# 5 # -----------------------------------#

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# выполнено 15.04.2020

currency = input('В какой валюте считать выручку? ')
revenue = int(input('Выручка : ') + str(f'{currency}'))
cost = int(input('Издержки: '))
profit = revenue - cost

if revenue > cost:
    print('Молодец')
    if profit > 0:
        rent = profit / a * 100
        print(f'Рентабельность {rent} %')
    staff = int(input('Человек: '))
    staff_1 = profit / staff
    print(f'Прибыль на одного сотрудника {staff_1} {currency}')
else:
    print('Не молодец')

# -----------------------------------# 6 # -----------------------------------#

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# выполнено 15.04.2020

a = int(input('Километров в день: '))
b = int(input('Сколько километров надо пробежать: '))
day = 1

while a <= b:
    print(f'{day}-й день: {a:.2f}')
    a = a + a * 0.1
    day += 1
    day += 1

# -----------------------------------#
