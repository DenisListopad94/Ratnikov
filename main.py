#ДОМАШНЕЕ ЗАДАНИЕ №1
#1
print(("№1"), 17/2*3+2, 2+17/2*3, 19%4+15/2*3, 15+6-10*4, 17/2%2*3**3)
#2
print(("№2"), (17/2)*(3+2), (2+17)/2*3, 19%(4+15)/2*3, (15+6-10)*4, 17/2%(2*3**3))
#3
have = 11
bread = 1.50
print(("№3"), 11 - 3 * 1.50, "рублей осталось")
#4
anna = 2
pol = 5
print(("№4"), 'У Анны', anna, 'яблока,', 'у Пола', pol, 'яблок.')
#5
days = 5
print(("№5"), "5 суток =", days * 24, "часов =", days * 24 * 60, "минут =", days * 24 * 60 * 60, "секунд")
#6
days = 182
weeks = days // 7
print(("№6"), weeks, "полных недель")
#7
side_1 = int(input("Введите сторону a: "))
side_2 = int(input("Введите сторону b: "))
squre = 30
squres = (side_1 // 30) * (side_2 // 30)
print("№7", "Можно отрезать", squres, "квадратов")
#8
seconds = int(input("Введите количество секунд: "))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(("№8"), hours, "час", minutes, "минут", seconds, "секунд")
#9
cash = int(input("Cash: "))
hundred = cash // 100
cash %= 100
fifty = cash // 50
cash %= 50
ten = cash // 10
cash %= 10
one = cash // 1
cash %= 1
print(("№9"), hundred,"купюры по 100 рублей,", fifty, "купюра по 50 рублей,", ten, "купюра по 10 рублей,", one, "купюра по 1 рублю.")


#ДОМАШНЕЕ ЗАДАНИЕ №2
#1
stroka = "123456789"
print("Задание №1:")
print(stroka[2])
print(stroka[-2])
print(stroka[:5])
print(stroka[:-2])
print(stroka[::2])
print(stroka[1::2])
print(stroka[::-1])
print(stroka[-1::-2])
print(len(stroka))

#2
meen = "cola"
print("Задание №2", meen[0] == meen[-1])

#3
slovo = "computer"
print("Задание №3", slovo[1:4])

#4
apple = "яблоко"
print("Задание №4", apple[1:5], apple[3:6])

#5
person = "Ivanou Ivan"
print("Задание №5", person.split()[::-1])


#6
word = "шалаш"
print("Задание №6", word, word[::-1])

#7
spisok = ["zero", "two", "five"]
print("Задание №7", spisok[1])

#8
s_1 = "employ"
s_2 = "employment"
s_full = s_1 in s_2
print("Задание №8", s_full)

#9
st_0 = "sdfghfhgfd"
in_0 = st_0.find("f")
in_1 = st_0.find("f", in_0 + 1)
print("Задание №9", in_1)

#10
school = {"1a": 25,
          "2б": 23,
          "3в": 21,
          "4г": 22,
          "5б": 20,
          "6а": 24,
          "7в": 22,
          "8б": 25,
          "9а": 23,
          "10б": 13,
}
school["5б"] = 28
school.update({"10в": 12})
school.pop("4г")
print("Задание №10", school, "Oбщее количество учащихся:", sum(school.values()))


#2HARD
a = 5
b = 6
N = 4
c = ((a + 1) * (b + 1) - a - b - a * b) ** N
print("ЗаданиеHARD2", c)

#4HARD
stroka = "My name is TheLastStylebender"
t_p = tuple(stroka)
print("ЗаданиеHARD4", t_p.count("e"))


#ДОМАШНЕЕ ЗАДАНИЕ №3(task 4)

#1
A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))
if A < 0:
    print("TRUE")
elif B < 0:
    print("TRUE")
elif C < 0:
    print("TRUE")
else:
    print("FALSE")

#2
n = int(input("Ввести целое число n:"))
k = int(input("Ввести целое число k:"))
if n % 2 == k % 2:
    print('TRUE')
else:
    print("FALSE")

#3
a = int(input("Ввести целое число a:"))
b = int(input("Ввести целое число b:"))
c = int(input("Ввести целое число c:"))
chet = 0
if a % 2 == 0:
    chet += 1
if b % 2 == 0:
    chet += 1
if c % 2 == 0:
    chet += 1
print(chet)

#4
q = int(input("Ввести двузначное число:"))
c = q // 10
b = q % 10
sum = c + b
if sum > 9:
    print("ДА")
else:
    print("НЕТ")

#5
for i in range(20):
    print("10")

#6
N = int(input("N="))
for i in range(1, N):
    print(i ** 3, end = ",")

#7
c = 1
for i in range(5, 21):
    c *= i
    print(c)

#8
n = int(input("n="))
c = 1
while c ** 2 < n:
    print(c ** 2)
    c += 1

#9
n = int(input("Ввести натуральное число:"))
min = min(str(n))
print(min)


#10
year = int(input("Ввести год:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Не високосный")

#11
n = int(input("Ввести натуральное число:"))
if n % 10 == 1:
    print("На лугу", n , "корова")
elif n % 10 == 2:
    print("На лугу", n, "коровы")
elif n % 10 == 3:
    print("На лугу", n, "коровы")
elif n % 10 == 4:
    print("На лугу", n, "коровы")
else:
    print("На лугу", n, "коров")

#не получается((

#ДОМАШНЕЕ ЗАДАНИЕ №3(task 5)

#1
numbers = (6, 2, 7, 8)
for num in numbers:
    delit = 0
    for i in range(1, num):
        if num % 1 == 0:
            delit += i
            if delit == num:
                print(num)
#2
numbers = (5, 2, -2, 7, -8, -9, 1)
counter = 0

for i in range(len(numbers)):
    if numbers[i-1] < 0 and numbers[i] >= 0 or numbers[i-1] >= 0 and numbers[i] < 0:
        counter += 1

print(counter)

#3
list1 = [4, 1, 6, 9]
list2 = [8, 1, 2, 4, 9, 5, 7, 6]
elements = []
for element in list1:
    if element not in list2:
        elements.append(element)

if elements:
    min_element = min(elements)
    print(min_element)
else:
    print("нет такого элемента")

#4
l = [12, 33, 39, 11, 46, 78]
p = []
for num in l:
    p.append(num)
    if num % 2 == 0:
        num = int(str(num)[::-1])
        p.append(num)
print(p)

#5
a = [5,2,4,5,1,2]
new_a = set(a)
counter = 0
for i in new_a:
    counter = a.count(i)
    print(i, counter)

#6
s_p = [7, 4, 1]
new_sp = []
for i in s_p:
    new_sp.append(i)
    new_sp.append(0)
print(new_sp)

#7
s_0 = '21 212 34 55 66 21'
number = s_0.split()
new = set()
for num in number:
    if num in new:
        print("yep")
    else:
        new.add(num)
        print('no')

#9
synonyms_dict = {
    'happy': 'funny',
    'smart': 'intelligent',
    'fast': 'quick',
    'big': 'large',
    'tall': 'high'
}


word_to_find = input("Введите слово, для которого нужно найти синоним: ")

if word_to_find in synonyms_dict:
    synonym = synonyms_dict[word_to_find]
    print(word_to_find, synonym)
else:
    print("Синоним для слова", word_to_find, "не найден")



#2
spis_0 =[5,2,0,-2,-7,1,8,0,-1]
poz = []
neg = []
zero = []
for i in spis_0:
    if i > 0:
        poz.append(i)
    elif i == 0:
        zero.append(i)
    else:
         neg.append(i)

new_spis = poz + neg + zero
print(new_spis)

#3
list_1 = [5,2,7,3,8,2,4,1,6,5]
list_2 = []
for i in list_1:
    if list_1.count(i) == 1:
        list_2.extend([i, i])
    else:
        list_2.append(i)
print(list_2)

#ДОМАШНЕЕ ЗАДАНИЕ(ФУНКЦИИ ЧАСТЬ 1)
#1
def stepen()-> list[int]:
    '''Функция генерирует список из 10 чисел во второй степени'''
    a = [i ** 2 for i in range(1,11)]
    return a
r_1 = stepen()
print(r_1)

#2
def krat()-> list[int]:
    '''Функция генерирует список из всех трехзначных чисел, которые кратны 3 и 5'''
    b = [i for i in range(100, 1000) if i % 3 == 0 and i % 5 == 0]
    return b
r_2 = krat()
print(r_2)

#3
def numbers(a:int,b:int,c:int):
    '''Функция создает список чисел из промежутка от а до b в степени с'''
    result = []
    for num in range(a, b + 1):
        result.append(num ** c)
    print(result)
a, b, c = map(int,input('Введите a b c через пробел: ').split())
numbers(a,b,c)

#5
'''
Напишите функцию, для нахождения минимального элемента из 2 чисел.
С помощью данной функции найдите минимальное четырёх чисел.
'''
def min(var_1: int, var_2: int) -> int:
    if var_1 < var_2:
        return var_1
    else:
        return var_2

min_two = min(1, 4), min(5, 2)
print(min_two)

#6
'''
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа и
выведите результат работы этой функции.
'''
import math
def distance(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt((x2 - x1)**2 + (y2 - y1) **2)

print(distance(2,5,2,3))

#7
'''
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
Ищем число Фиббоначи через цикл! Рекурсию не использовать!
'''
def fib(n):
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

print(fib(9))


'''
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x 
и возвращающую самое маленькое целое число y, такое что:
-y больше или равно x
-y делится нацело на 5
'''
#8
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x + (5 - x % 5)

print(closest_mod_5(16))

#9
'''Функция считывает список чисел, удаляет все нечетные числа, а четные нацело делит на 2'''
def modify_list(l):
    l = [i // 2 for i in l if i % 2 == 0]
    print(l)

modify_list([1,2,3,4,5,6,7,8,9])

#11(доп.)
'''	*Сгенерировать список всех простых чисел до  100.'''
def prostoe():
    return [num for num in range(2, 101) if all(num % i != 0 for i in range(2, num))]

p = prostoe()
print(p)


#(ФУНКЦИИ ЧАСТЬ 2)

#1
'''Создайте lambda-функцию для нахождения подстроки в введённой строке.'''
find_podstr = lambda main_str, podstr: podstr in main_str
main_str = (input("Ввести строку:"))
podstr = (input("Ввести подстроку:"))

f_p = find_podstr(main_str, podstr)
print(f_p)

#2
'''	Проверьте число на чётность с помощью анонимной функции.'''
chet = lambda x: x % 2 == 0
number = int(input("Введите число:"))
check = chet(number)
print(check)

#3
'''
Напишите lambda-функцию, которая будет приветствовать пользователя 
имя которого введено корректно, с большой буквы.
Иначе будет выводить сообщение о неверно введённом имени.
'''
hello = lambda name: f"Привет, {name}!" if name and name.istitle() else "Неверно введено имя."
user_name = input("Введите ваше имя: ")
result = hello(user_name)
print(result)

#4
'''
Напишите рекурсивную функцию digits(n), 
которая принимает натуральное число и возвращает строку
с цифрамиэ того числа справа налево, разделяя их пробелами.
'''
def digits(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + " " + digits(n // 10)


result = digits(123456)
print(result)

#5
'''
Напишите рекурсивную функцию is_power(n), 
которая возвращает True, если переданное натуральное число
является степенью двойки, и False иначе
'''
def is_power(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n < 1:
        return False
    else:
        return is_power(n // 2)

ret = is_power(18)
print(ret)

#6
'''Дано натуральное число N. Вычислите сумму его цифр'''
def nchislo(n):
    schet = 0
    while n > 0:
       num = n % 10
       schet += num
       n //= 10
    return schet

number = nchislo(3456)
print(number)

#7
'''
Дана функция, которая выводит все простые числа в промежутке от 1 до 100. 
Написать декоратор который будет проверять время работы этой функции.
Задекорировать функцию. Вывести вpемя работы этой функции, а так же сами простые числа.
'''
import datetime
def time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        time = end_time - start_time
        print(f"Время работы функции: {time}")
        return result
    return wrapper

@time
def prostoe():
    return [num for num in range(2, 101) if all(num % i != 0 for i in range(2, num))]

print(prostoe())
#8
'''
Дана функция, которая проверяет введённый пользователем пароль.
Задекорировать её так, чтобы при правильно введённом пароле
она приветствовала пользователя.
'''
def password_decorator(func):
    def wrapper(password):
        correct_password = "stylebender"
        if password == correct_password:
            print("Пароль введен верно.")
            func(password)
        else:
            print("Неверный пароль. Вход запрещен.")
    return wrapper

@password_decorator
def greet_user(password):
    print("Привет, пользователь!")

user_input = input("Введите пароль: ")
greet_user(password=user_input)


#ДОМАШНЕЕ ЗАДАНИЕ(TASK_8)
#1
'''
Имеется текстовый файл. Получить текст, в котором в конце каждой
строки из заданного файла добавлен восклицательный знак.
'''

with open('ex1.txt', "r", encoding='utf-8') as file:
    lines = file.readlines()

new_lines = [line.strip() for line in lines if "!" in line]

for line in new_lines:
    print(line)

#2
"""
Создать файл input.txt и записать в него 10 чисел через пробел. 
Считать из него эти числа. Затем записать их произведение в файл output.txt.
"""
with open('input.txt', 'w') as i_file:
    numbers = " ".join(map(str, range(1, 11)))
    i_file.write(numbers)

with open('input.txt', 'r') as i_file:
    new = i_file.readline()
    new_num = list(map(int, new.split()))

num = 1
for i in new_num:
    num *= i

with open('output.txt', 'w') as o_file:
    o_file.write(str(num))

#3
"""
Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, 
цену единицы и дату поступления товара на склад.
Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р.
"""
from datetime import datetime

products_list = [
    {"Наименование": "Товар1", "Количество": 100, "Цена за единицу": 1000, "Дата поступления": "2023-01-15"},
    {"Наименование": "Товар2", "Количество": 50, "Цена за единицу": 30000, "Дата поступления": "2023-12-20"},
    {"Наименование": "Товар3", "Количество": 150, "Цена за единицу": 2500000, "Дата поступления": "2023-02-20"},
    {"Наименование": "Товар4", "Количество": 50, "Цена за единицу": 3000000, "Дата поступления": "2023-02-20"},
    {"Наименование": "Товар5", "Количество": 250, "Цена за единицу": 30000, "Дата поступления": "2023-12-20"},
]

current_date = datetime.now()

with open("file.txt", "w", encoding='utf-8') as t_file:
     new = t_file.write(str(products_list))


filtered_products = [
    product for product in products_list
    if (current_date - datetime.strptime(product["Дата поступления"], "%Y-%m-%d")).days > 30
    and product["Количество"] * product["Цена за единицу"] > 1000000
]


for item in filtered_products:
    print(item)

#4
import json

new_dict = { 12345: ("Vlad", 21),
             54321: ("Dima", 23),
             22334: ("Arthur", 25),
             88134: ("Kate", 19),
             73453: ("Lina", 22)
}

with open("file.json", "w") as j_file:
    json.dump(new_dict, j_file)

#5
"""
Прочитать сохранённый json – файл и записать данные на диск в csv файл. 
Первое значение каждой строки должно начинаться со слова person, значения разделить 
"""
import json
import csv

with open("file.json", "r") as j2_file:
    read_j = json.load(j2_file)

csv_file_path = 'file.csv'
with open(csv_file_path, "w", encoding='utf-8') as cs_file:
    write_csv = csv.writer(cs_file, delimiter=',')


    for key, value in read_j.items():
        write_csv.writerow(['person', key] + list(value))

#6
""" Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали."""
try:
    x = (1, 2, 5, 7)
    x = x / 2
    print(x)

except Exception as e:
    print(e)

#7
"""
Напишите программу которые будет ловить IndexError,
когда вы пытаетесь взять индекс элемента, которого нет в списке.
"""

try:
    spisok = [1, 2, 3, 4]
    print(spisok[4])
except IndexError:
    print("Ошибка IndexError")

#8
"""
Напишите программу которые будет ловить TypeError,
когда вы пытаетесь скаткатенировать строку и число.
"""

try:
    st = "Sheeesh" + 44
    print(st)
except TypeError:
    print("Ошибка TypeError")

#9
'''
Напишите программу которые будет ловить FileNotFoundError, 
когда вы пытаетесь открыть файл для чтения, которого не существует.
'''

try:
    with open("nofile.txt", "r") as file:
        files = file.readline()
except FileNotFoundError:
    print("Ошибка FileNotFoundError")

#10
'''
Дан список. Пользователь не знает его размер.
Программа должна бросить исключение TypeError,
когда пользователь пытается удалить элемент которого нет в списке
'''

spis_2 = [21, 2, 3, 45, 54, 32, 1]
element = int(input("Введите элемент для удаления:"))
if element not in spis_2:
    raise TypeError


#ДОМАШНЕЕ ЗАДАНИЕ(TASK_9)

#1
'''
Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
'''

class Numbers:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def printf(self):
        print(f"a = {self.a}")
        print(f"b = {self.b}")

    def changes(self):
        if self.a > 0 and self.b > 0:
            print(self.a + 6, self.b + 9)

    def summa(self):
        print(f"Сумма чисел {self.a + self.b}")

    def maxz(self):
        if (self.a > self.b):
            print(f"max = {self.a}")
        else:
            print(f"max = {self.b}")


m = Numbers(1, 2)
m.printf()
m.changes()
m.summa()
m.maxz()

#2
'''
Описать класс, реализующий десятичный счетчик,
который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне. 
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. 
Написать программу, демонстрирующую все возможности класса.
'''
class Counter:
    def __init__(self, minimum=0, maximum=10, value=8):
        self.minimum = minimum
        self.maximum = maximum
        self.value = value if value is not None else minimum

    def defaultnum(self):
        print(f"Текущее значение {self.value}")

    def high(self):
        self.value = min(self.value + 1, self.maximum)
        print(f"увеличение {self.value}")

    def low(self):
        self.value = max(self.value - 1, self.minimum)
        print(f"уменьшение {self.value}")

counter_custom = Counter()
counter_custom.defaultnum()
counter_custom.high()
counter_custom.low()


#3
'''
Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, 
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
'''
class Shop:
    def __init__(self):
        self.products = []

    def addprod(self, product_name):
        self.products.append(product_name)
        print(f"{product_name} добавлен в магазин")

    def searchprod(self, product_name):
        if product_name in self.products:
            print(f"{product_name} найден в магазине.")
        else:
            print(f"{product_name} не найден в магазине.")

    def delprod(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)
            print(f"{product_name} удален из магазина.")



shop = Shop()

shop.addprod("Яблоко")
shop.addprod("Молоко")
shop.addprod("Хлеб")

shop.searchprod("Молоко")
shop.searchprod("Масло")

shop.delprod("Молоко")

#4
"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой. 
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, 
предоставлять возможность добавлять монеты в копилку и узнавать, 
можно ли добавить в копилку ещё какое-то количество монет,
не превышая ее вместимость. 
"""

class MoneyBox:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.coins_inside = 0

    def can_add(self, v):
        return self.coins_inside + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins_inside += v
            print(f"Добавлено {v} монет. Текущее количество монет: {self.coins_inside}")
        else:
            print("Невозможно добавить указанное количество монет.")


cash = MoneyBox()
cash.add(5)
cash.add(6)

#ДОМАШНЕЕ ЗАДАНИЕ(TASK_10)
# 1
'''
Создайте систему управления задачами с использованием классов.
Реализуйте классы "Task", "Project" и "ProjectManager". Каждая задача должна содержать описание,
статус (выполнена или нет) и срок выполнения.
Проект должен включать в себя список задач и методы для добавления новой задачи,
отметки задачи как выполненной и вывода списка всех задач.
'''


class Task:
    def __init__(self, description, status, deadline):
        self.description = description
        self.status = status
        self.deadline = deadline

    def get_info(self):
        print("Описание:", self.description, ". Cтатус:", self.status, ". Срок выполнения:", self.deadline)


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def done_or_not(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                print(f"Задача {task_description} выполнена")
            else:
                print("Задача не выполнена")

    def show_tasks(self):
        for task in self.tasks:
            print(task)


class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, project_name):
        project = Project(project_name)
        self.projects.append(project)
        print(f"Создан новый проект: '{project_name}'.")


project = ProjectManager()
project.create_project("ЗАДАНИЕ_1")
n_1 = Task("New project for our company", "Active", "02.02.2024")
n_1.get_info()

# 2
"""
Создайте систему для управления бронированием билетов в авиакомпании. 
Реализуйте классы "Passenger", "Ticket", "Flight" и "Airline ". Каждый пассажир должен иметь атрибуты, 
такие как имя и фамилия. Билет должен содержать информацию о пассажире и маршруте полета. 
Рейс должен включать в себя список зарезервированных билетов.
Авиакомпания должна иметь методы для бронирования билета, отмены брони и отображения списка зарезервированных билетов.
"""

class Passenger:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        print("Информация о пассажире:", self.name, self.surname)


class Ticket(Passenger):
    def __init__(self, name, surname, flight_route):
        super(Ticket, self).__init__(name, surname)
        self.flight_route = flight_route

    def get_info(self):
        super().get_info()
        print("Информация о маршруте полета:", self.flight_route)


class Airline(Ticket):
    def __init__(self, name, surname, flight_route):
        super(Airline, self).__init__(name, surname, flight_route)
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)

    def get_info(self):
        super().get_info()
        print(self.tickets)

    def list_ticket(self):
        print("Список зарезервированных билетов:", self.tickets)


class Flight(Airline):
    def __init__(self, name, surname, flight_route):
        super(Flight, self).__init__(name, surname, flight_route)
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)

    def list_ticket(self):
        print("Список зарезервированных билетов:", self.tickets)


inf = Airline('Vlad', "Ratnikov", 'From Belarus to Russia')
inf.add_ticket("Ticket1")
inf.get_info()
inf.list_ticket()

# 3
"""
Создать абстрактный класс «Alive». Определить наследуемые классы – «Fox», «Rabbit» и «Plant».
Лисы едят кроликов. Кролики едят растения. Растение поглощают солнечный свет.
Представители каждого класса могут умереть, если достигнут определенного возраста или для них не будет еды.
Напишите виртуальные методы поедания и определения состояния живых существа
(живые или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
"""

from abc import ABC, abstractmethod


class Alive(ABC):
    def __init__(self, age):
        self.age = age
        self.alive = True

    @abstractmethod
    def eat(self, food_available):
        pass

    def check_status(self, food_available):
        if self.age >= self.max_age or not food_available:
            self.alive = False
            print(f"{self.__class__.__name__} больше не живет.")
        else:
            print(f"{self.__class__.__name__} живет.")


class Fox(Alive):
    def __init__(self, age):
        super().__init__(age)
        self.max_age = 5

    def eat(self, food_available):
        if food_available:
            print("Лиса ест кролика.")
        else:
            print("Для лисы нет еды.")


class Rabbit(Alive):
    def __init__(self, age):
        super().__init__(age)
        self.max_age = 3

    def eat(self, food_available):
        if food_available:
            print("Кролик ест растение.")
        else:
            print("Для кролика нет еды.")


class Plant(Alive):
    def __init__(self, age):
        super().__init__(age)
        self.max_age = 2

    def eat(self, food_available):
        if food_available:
            print("Растение поглащают солнечный свет.")
        else:
            print("Для растения нет солнечного света.")


fox = Fox(age=3)
rabbit = Rabbit(age=2)
plants = Plant(age=1)

fox.eat(food_available=True)
fox.check_status(food_available=True)

rabbit.eat(food_available=True)
rabbit.check_status(food_available=True)

plants.eat(food_available=False)
plants.check_status(food_available=False)

#ДОМАШНЯЯ РАБОТА(TASK_11)
#1
"""
Напишите функцию fib, которая будет выводить последовательно каждое число Фиббоначи.
"""
def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = list(fib_generator(10))
print(fib)

#2
"""
Напишите функцию simple, которая будет выводить поочерёдно простые числа
от 2 до введённого числа n до вызова исключения.
"""
def simple(p):
    current_number = 2
    while current_number <= p:
        if all(current_number % i != 0 for i in range(2, int(current_number**0.5) + 1)):
            yield current_number
        current_number += 1
try:
    for prime_number in simple(20):
        print(prime_number, end=" ")
except StopIteration as e:
    pass

#3
"""
Напишите генератор для вывода всех совершенных чисел до 1000000000.
"""

def generator(n):
    number = 2
    while number <= n:
        divisors_sum = sum(i for i in range(1, number) if number % i == 0)
        if divisors_sum == number:
            yield number
        number += 1

for perfect_number in generator(1000000000):
    print(perfect_number, end=" ")

#4
"""
Исключить из строки группы символов, расположенные между первыми символами '{' и '}' вместе со скобками.
Если нет символа '}', то исключить все символы до конца строки после '{'.
Вывести символ, наиболее часто встречающийся в строке.
"""
from collections import Counter

def process_string(our_str):
     open = our_str.find('{')
     close = our_str.find('}', open)

     if open != -1 and close != -1:
         new_str = our_str[:open] + our_str[close + 1:]
     elif open != -1:
         new_str = our_str[:open]
     else:
         new_str = our_str

     new_our_str = new_str.replace(" ", "")
     ct = Counter(new_our_str)
     most_common = ct.most_common(1)

     return new_str, most_common

i_s = "Hello {don't} play {with} me."
result, most_common = process_string(i_s)

print("Строка:", result)
print("Cимвол часто встречающийся в строке и сколько раз:", most_common)

#6
"""
Используя list comprehension. Сгенерируйте список как показано ниже:

1    1    1    1     1    1
1    2    3    4     5    6
1    3    6   10  15    21
1   4   10   20  35    56
1   6   21   56  126  252
"""

rows = 5
cols = 6

matrix = [[1 if j == 1 else 1 for j in range(cols)] for _ in range(rows)]

for i in range(1, rows):
    for j in range(1, cols):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for row in matrix:
    print(row)


#7
"""
Коля понял, что у многих из его знакомых есть несколько телефонных номеров
и нельзя хранить только один из них. Он попросил доработать Вашу программу так, 
чтобы можно было добавлять к существующему контакту новый номер или даже несколько номеров, 
которые передаются через запятую. По запросу телефонного номера должен выводиться весь список номеров
в порядке добавления, номера должны разделяться запятой. 
Если у контакта нет телефонных номеров, должна выводиться строка "Не найдено".
"""

class Contact:
    def __init__(self):
        self.phone_numbers = []

    def add_phone_numbers(self, numbers):
        new_numbers = [number.strip() for number in numbers.split(",")]
        self.phone_numbers.extend(new_numbers)

    def get_phone_numbers(self):
        if not self.phone_numbers:
            return "Не найдено"
        return ", ".join(self.phone_numbers)


contacts = {}

while True:
    name = input("Введите имя контакта (или 'exit' для завершения): ")

    if name.lower() == 'exit':
        break

    if name not in contacts:
        contacts[name] = Contact()

    action = input("Выберите действие: 1) Добавить номер, 2) Получить номера: ")

    if action == '1':
        numbers_to_add = input("Введите номер через запятую: ")
        contacts[name].add_phone_numbers(numbers_to_add)
    elif action == '2':
        phone_numbers = contacts[name].get_phone_numbers()
        print(f"Телефонные номера для контакта {name}: {phone_numbers}")
    else:
        print("Некорректное действие. Повторите ввод.")

