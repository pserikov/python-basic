
__author__ = 'Сериков Павел Евгеньевич'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

rus_cap = list(map(chr, range(ord('А'), ord('Я')+1)))
no_cap = ('Й', 'Ъ', 'Ы', 'Ь')

# Уберем из списка буквы, на которые нет слов.
for el in no_cap:
	rus_cap.remove(el)

print(rus_cap)

# Сразу сделаем файлы, которые будем заполнять.
for i in rus_cap:
	path = os.path.join('data', 'fruits' + '_' + i)
	f = open(path, 'w', encoding = 'UTF-8')
	f.close()	 

# Сделаем список фруктов из входного файла.
path_in = os.path.join('data', 'fruits')
f = open(path_in, 'r', encoding = 'UTF-8')
fruits = f.readlines()
f.close()

print(fruits)

print(fruits[0][0], type(fruits[0][0]))

# Пройдем по списку фруктов и по первой букве поместим в соответствующий файл.
for i in fruits:
	for j in rus_cap:
		if i[0] == j:
			path = os.path.join('data', 'fruits' + '_' + j)
			f = open(path, 'a', encoding = 'UTF-8')
			f.write(i)
			f.close()

