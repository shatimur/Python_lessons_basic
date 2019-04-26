# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

# Решение 1:

import os

workers_file = os.path.join('data', 'workers')
hours_file = os.path.join('data', 'hours_of')

hours = []
workers = []

with open(hours_file, 'r', encoding='UTF-8') as f:      # создаем список с данными по ФИО и отработанным часам
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            hours.append(line[:-1])
        else:
            hours.append(line)

with open(workers_file, 'r', encoding='UTF-8') as f:    # создаем список с данными по ФИО и должностям и базовому окладу
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            workers.append(line[:-1])
        else:
            workers.append(line)

full_workers = []

for itm in workers:
    for itm2 in hours:
        if itm.split()[0] in itm2 and itm.split()[1] in itm2:
            full_workers.append(itm + ' ' + itm2.split()[-1])   # список из двух файлов, где создержатся все данные по
                                                                # работникам, включая отработанные часы


class Staff:

    def __init__(self, worker_data):
        worker_data = worker_data.split()
        self.name = worker_data[0]
        self.surname = worker_data[1]
        self.full_salary = int(worker_data[2])
        self.post = worker_data[3]
        self.hours_rule = int(worker_data[4])
        self.hours_done = int(worker_data[5])

    @property
    def calculate_salary(self):
        salary = 0
        if self.hours_done < self.hours_rule:
            salary = self.full_salary * (self.hours_done/self.hours_rule)
        elif self.hours_done == self.hours_rule:
            salary = self.full_salary
        else:
            salary = self.full_salary + ((self.hours_done - self.hours_rule) * (self.full_salary/self.hours_rule))
        return round(salary, 2)


workers_lst = [Staff(itm) for itm in full_workers]   # создаем список объектов Staff

print(full_workers)


def factory_salary(lst):    # узнать общий фонд оплаты труда
    common_salary = 0
    for itm in lst:
        a = itm.calculate_salary
        common_salary += a
    return common_salary



# a = workers_lst[1].calculate_salary
# print(a)
# print(factory_salary(workers_lst))


# Решение 2

import os

workers_file = os.path.join('data', 'workers')      # путь к файлу работников
hours_file = os.path.join('data', 'hours_of')       # путь к файлу отработанных часов

workers = []

with open(workers_file, 'r', encoding='UTF-8') as f:    # создаем список с данными по ФИО и должностям и базовому окладу
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            workers.append(line[:-1])
        else:
            workers.append(line)

class Staff:

    def __init__(self, worker_data):
        worker_data = worker_data.split()
        self.name = worker_data[0]
        self.surname = worker_data[1]
        self.full_salary = int(worker_data[2])
        self.post = worker_data[3]
        self.hours_rule = int(worker_data[4])

    @property
    def hours_worked(self):
        hours_worked = 0
        with open(hours_file, 'r', encoding='UTF-8') as f:
            for line in f:
                if self.name in line and self.surname in line:
                    hours_worked = int(line.split()[-1])
        return hours_worked

    @property
    def calculate_salary(self): # вычисляем зарплату конкретного рабочего
        salary = 0
        if self.hours_worked < self.hours_rule:
            salary = self.full_salary * (self.hours_worked/self.hours_rule)
        elif self.hours_worked == self.hours_rule:
            salary = self.full_salary
        else:
            salary = self.full_salary + ((self.hours_worked - self.hours_rule) * (self.full_salary/self.hours_rule))
        return round(salary, 2)     # не оформляем красиво в виде строки, чтобы можно было использовать в расчетах

workers_lst = [Staff(itm) for itm in workers]   # создаем список объектов Staff

def factory_salary(lst):
    s = 0
    for itm in workers_lst:
        s += itm.calculate_salary
    return f'ФОТ всей фабрики составляет {s}'

# a = workers_lst[4].calculate_salary
#
# b = factory_salary(workers_lst)
# print(a)
# print(b)