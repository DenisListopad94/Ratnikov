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