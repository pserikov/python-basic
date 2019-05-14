
__author__ = 'Сериков Павел Евгеньевич'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil # Для копирования файлов в Задаче-3

def make_dir(dir_name):
	os.mkdir(dir_name)

def del_dir(dir_name):
	os.rmdir(dir_name)

def prn_dir(dir_name='.'):
	print (os.listdir(dir_name))

def chg_dir(dir_name):
    os.chdir(dir_name)

# для копирвания файлов (Задача-3) воспользуюсь кодом из
# предыдущего курса "Python быстрый старт"
def file_copy(filename):        # Функция дублирования файла в *.copy
    if os.path.isfile(filename):
        newfile = filename + '.copy'
        shutil.copy(filename, newfile)
        print(filename + " --> " + newfile)
        if os.path.exists(newfile):
            print("Файл " + newfile + " успешно скопирован.")
            return True
        else:
            print("Проблема при копировании!")
            return False

if __name__ == "__main__":
    # получим текущую директорию
    cur_dir = os.getcwd()
    print(cur_dir)

    prn_dir(cur_dir)

    # создадим папки
    for i in range(1, 10):
        make_dir("dir_" + str(i))

    prn_dir(cur_dir)

    # удалим папки
    for i in range(1, 10):
        del_dir("dir_" + str(i))

    prn_dir(cur_dir)

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    dir_list = list(os.walk(cur_dir)) # соберем всю информацию о текущей деректории
    print("\n".join(dir_list[0][1])) # выведем только список папок из текущей директории

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    file_copy(__file__)
