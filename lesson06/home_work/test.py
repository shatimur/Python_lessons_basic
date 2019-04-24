# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

class Human:

    def __init__(self, name, surname, father=None, mother=None):
        self.name = name
        self.surname = surname
        self.father = father
        self.mother = mother


class Teacher(Human):

    def __init__(self, subject, name, surname, father=None, mother=None):
        self.subject = subject
        Human.__init__(self, name=name, surname=surname, father=father, mother=mother)


class Student(Human):

    def __init__(self, name, surname, father=None, mother=None, school_class=None):
        self.school_class = school_class
        Human.__init__(self, name=name, surname=surname, father=father, mother=mother)


class Subject:

    def __init__(self, name):
        self.name = name


class SchoolClass:

    def __init__(self):
        self.teachers = []
        self.students = []


class School:

    def __init__(self):
        self.school_class = []


names = ["Иван", "Филипп", "Анатолий", "Анна", "Мария", "Тамара"]
surnames = [""]

s_classes = ['5A', '6B', '7C', '8D']

subject_list = [Subject(itm) for itm in ['математика', 'геометрия', 'ин-яз', 'физ-ра', 'информатика']]
school = School()

school.school_class.append([SchoolClass(itm) for itm in s_classes])

humans = [Human(name=random.choice(names), surname=random.choice(surnames) for _ in range(0,8)]

teachers = [Teacher(subject=random.choice(subject_list), name=random.choice(names), surname=random.choice(surnames)) for _ in range(0,6)]

commit