# ----------------------- # 1 # ----------------------- #

# 1. Создать класс TrafficLight (светофор) и определить у него один
# атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']
    t = [7, 2, 6]
    status = 0
    off = False
    def running(self):
        if self.status % 2 == 0:
            print(f'Color {self.__color[self.status]} is on')
            time.sleep(self.t[self.status] - self.t[1])
            print(f'Color {self.__color[self.status]} is blink')
            time.sleep(self.t[1])
        else:
            print(f'Color {self.__color[1]} is on')
            time.sleep(self.t[1])
        if self.status == 3:
            self.status = 0
        else:
            self.status += 1
        self.running()

# c = TrafficLight()
# c.running()

# ----------------------- # 2 # ----------------------- #

# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    """Сласс для расчета веса асфальта, для укладки дороги"""

    def __init__(self, _length, _width, _thickness, _weight):
        self.length = _length
        self.width = _width
        self.thickness = _thickness
        self.weight = _weight

    def mass(self):
        """Формула расчета"""
        self.mass1 = self.length * self.width * (self.weight / 1000) * self.thickness
        print(f'Для укладки дороги потребуется {str(self.mass1)} тонн асфальта.')

sum = Road(
        int(input('Введите длину дороги в метрах: ')),
        int(input('Введите ширину дорогив метрах: ')),
        int(input('Введите толщину дорожного покрытияв в cантиметрах: ')),
        int(input('Введите вес асфальта на 1 м2 в кг: '))
)
sum.mass()

# class Road:
#     """Класс для расчета веса асфальта, для укладки дороги"""
#     def __init__(self, length, width, thickness, weight):
#         """Свойства дороги"""
#         self._length = length
#         self._width = width
#         self._thickness = thickness
#         self._weight = weight
#
#     def mass(self):
#         """Формула расчета"""
#         self.mass1 = str(self._length) * self._width * (self._weight / 1000) * self._thickness
#         print(f'{str(self.mass1)} тонн.')
#
# try:
#     """Проверка на ошибки"""
#     mass2 = Road(
#         int(input('Введите длину дороги в метрах: ')),
#         int(input('Введите ширину дорогив метрах: ')),
#         int(input('Введите толщину дорожного покрытияв в cантиметрах: ')),
#         int(input('Введите вес асфальта на 1 м2 в кг: ')))
#
# except:
#     print('Некорректный ввод исходных значений.')

# ----------------------- # 3 # ----------------------- #

# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут
# должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на
# реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).


class Worker:
    """ Создание класса 'Работник' """
    def __init__(self, name, surname, position, bonus, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    """ Дочерний класс для обработки данных работника """

    def get_full_name(self):
        """ Получене полного имени сотрудника """
        return self.name + ' ' + self.surname

    def get_total_income(self):
        """ Данные о зарплате сотрудника """
        return float(self._income['wage']) + float(self._income['bonus'])

    def get_position(self):
        """ Данные о должности сотрудника """
        return self.position

# ----------------------- # 4 # ----------------------- #

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    """ Создание класса Автомобиль """
    def __init__(self, speed, color, name, is_police, speed_now):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed_now = speed_now

    def go(self):
        """ Расчет скорости """
        speed_question = input('Gas or brakes? ')
        if speed_question == 'Gas' or 'gas':
            print(f'Еhe car is started and ready to go. Speed is {str(self.speed)} км/ч')
            self.speed_now = input('What speed to dial? ')
            print(f'Your speed {self.speed_now} km / h')
            if int(self.speed_now) > 60:
                print(f'Your speed is {int(self.speed_now) - 60} higher than the limit')
                speed_question = input('Do you want to slow down to the speed limit? Yes or No ').lower()
                if speed_question == 'yes':
                    self.speed = 60
                    print(f'Your speed {int(self.speed)} km/h')
                elif speed_question == 'no':
                    self.speed = self.speed_now
                    print(f'Your speed {int(self.speed)} km/h')

        elif speed_question == 'brakes':
            self.speed = 0
            print(f'Your speed {str(self.speed)} km/h')
        else:
            print('Select the gas or brake')

    def stop(self):
        """ Остановка двигателя """
        print('engine off. ')
        self.speed = 0

    def turn(self):
        """ Повороты """
        turn1 = input('Where to turn right or left? ')
        if turn1 == 'right':
            print('You turned right. ')
        else:
            print('You turned left. ')

    def show_speed(self):
        """ Вывод скорости автомобиля """
        print(f'Car speed is {str(self.speed)} km/h')

    def speed_up(self):
        """ Изменение скорости """
        self.speed += 10

class TownCar(Car):
    """ Городской автомобиль """

    def show_speed(self):
        """ Скорость обычного авто """
        if self.speed > 60:
            print(f'Your speed is {int(self.speed) - 60} higher than the limit')
        else:
            print(f'Your speed {self.speed_now} km / h')

class SportCar(TownCar):
    """ Sportcar """

    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is {int(self.speed) - 60} higher than the limit')
        else:
            print(f'Your speed {self.speed} km / h')

class WorkCar(TownCar):
    """ Workcar """

    def show_speed(self):
        """ Скорость рабочего авто """
        if self.speed > 40:
            print(f'Your speed is {int(self.speed) - 40} higher than the limit')
        else:
            print(f'Your speed {self.speed} km / h')

class PoliceCar(TownCar):
    def show_speed(self):
        """ Скорость полицейской машины """
        print(f'Car speed is {str(self.speed)} км/ч')

# ----------------------- # 5 # ----------------------- #

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        self.title = 'канцелярскими принадлежностями'
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        self.title = 'ручкой'
        print(f'Рисование {self.title}.')

class Pencil(Stationery):
    def draw(self):
        self.title = 'карандашом'
        print(f'Рисование {self.title}.')

class Handle(Stationery):
    def draw(self):
        self.title = 'маркером'
        print(f'Рисование {self.title}.')

# ----------------------- #   # ----------------------- #