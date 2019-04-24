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



# Школа
# Класс
# Предмет
# Учитель
# Студент
# Хуман
# Учитель, студент наследуется от  хуман
# Школа содержит атрибут классы
# Класс содержит атрибуты: преподаватели , ученики
# Учитель содержит атрибут предмет

class School:
    def __init__(self, classes):
        self.classes = classes

class Class_room:
    def __init__(self, class_name):
        self.class_name = class_name
        self.teachers = []
        self.students = []
        School.classes += 1

class Subject:
    def __init__(self, teachers):
        self.teachers = teachers

class Human:
    def __init__(self, full_name):
        self.name = self.full_name.split()[0]
        self.surname = self.full_name.split()[1]

class Student(Human):
    def __init__(self, full_name, class_room, subjects):
        Human.__init__(self, full_name)
        self.class_room = class_room
        self.subjects = subjects

class Teacher(Human):
    def __init__(self, full_name, subject):
        Human.__init__(self, full_name)
        self.subject = subject