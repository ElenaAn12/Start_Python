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