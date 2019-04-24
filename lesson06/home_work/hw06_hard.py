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

class Staff:

    def __init__(self, name, surname, full_salary, hours_worked):
        self.name = name
        self.surname = surname
        self.full_salary = full_salary
        self.hours_worked = hours_worked


class Foreman(Staff):

    def __init__(self, post, name, surname, full_salary, hours_worked):
        self.post = post
        Staff.__init__(self, name, surname, full_salary, hours_worked)


class Carpenter(Staff):

    def __init__(self, hours_to_work, name, surname, full_salary, hours_worked):
        self.hours_to_work = hours_to_work
        Staff.__init__(self, name, surname, full_salary, hours_worked)


class Chief(Staff):




class Worker(Staff):
    pass