# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#  готово cp <file_name> - создает копию указанного файла
#  готово rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#  готово cd <full_path or relative_path> - меняет текущую директорию на указанную
#  готово ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile
print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копия файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> сменить директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def delete_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.remove(file_path)
        print('Файл {} успешно удален'.format(file_name))
    except FileNotFoundError:
        print('Невозможно удалить {} - такой файл не существует'.format(file_name))

def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(path)
        print('Вы успешно перешли в директорию {}'.format(dir_name))
        print(os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти в {} - такой директории не существует'.format(dir_name))

def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_name_copy = str("copy_" + file_name)
    file_path = os.path.join(os.getcwd(), file_name_copy)
    try:
        copyfile(file_name, file_path)
        print('файл {} создан'.format(file_name_copy))
    except FileExistsError:
        print('файл {} уже существует'.format(file_name))
    except FileNotFoundError:
        print('файл {} не существует'.format(file_name))

def full_path():
    path = os.getcwd()
    print(path)

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "ls": full_path,
    "rm": delete_file,
    "cd": change_dir
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
