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
        if father:
            self.patr_name = father.name + 'ович'
        else:
            self.patr_name = 'Безотцовщина'


    @property
    def full_name(self):
        return f'{self.name} {self.surname} {self.patr_name}'


class Teacher(Human):

    def __init__(self, subject, name, surname, father=None, mother=None):
        self.subject = subject
        Human.__init__(self, name=name, surname=surname, father=father, mother=mother)


class Student(Human):

    def __init__(self, name, surname, father, mother, school_class=None):
        self.school_class = school_class
        Human.__init__(self, name=name, surname=surname, father=father, mother=mother)

    @property
    def get_subjects(self):
        return [itm.subject.name for itm in self.school_class.teachers]

    @property
    def get_parents(self):
        return [self.father.full_name, self.mother.full_name]


class Subject:

    def __init__(self, name):
        self.name = name


class SchoolClass:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    @property
    def get_subjects(self):
        return [itm.subject for itm in self.teachers]

    @property
    def get_students(self):
        return [itm.full_name for itm in self.students]

    @property
    def get_teachers(self):
        return [itm.full_name for itm in self.teachers]


class School:

    def __init__(self):
        self.school_classes = []

    @property
    def get_classes(self):
        return [itm.name for itm in self.school_classes]

    @property
    def get_students(self):
        list = []
        for itm in self.school_classes:
            for student in itm.students:
                list.append(student)
        return list

    def add_teacher(self, *teachers):
        for s_cls in self.school_classes:
            while len(s_cls.get_subjects) < len(set(teacher.subject for teacher in teachers)):
                teacher = random.choice(teachers)
                if teacher.subject not in s_cls.get_subjects:
                    s_cls.teachers.append(teacher)

    def add_student(self, *students):
        for s_cls in self.school_classes:
            while len(s_cls.students) < 10:
                student = random.choice(students)
                if student not in self.get_students:
                    s_cls.students.append(student)
                    student.school_class = s_cls


names = ['Иван', 'Филипп', 'Анатолий', 'Анна', 'Мария', 'Тамара', 'Максим', 'Петр', 'Кирил', 'Женя', 'Саша', 'Маша']
surnames = ['Сидоров', 'Антуанет', 'Питонов', 'Иванов', 'Джобс', 'Петров', 'Рыбкин', 'Сидоров', 'Ефимов', 'Ралько']
s_classes = ['5A', '6B', '7G', '8D']

humans = [Human(name=random.choice(names), surname=random.choice(surnames)) for _ in range(20)]

subjects_lst = [Subject(itm) for itm in ['математика', 'геометрия', 'Ин-яз', 'Физ-ра', 'Информатика']]

teachers = [Teacher(subject=random.choice(subjects_lst), name=random.choice(names), surname=random.choice(surnames),
                    father=random.choice(humans), mother=random.choice(humans)) for _ in range(15)]

school = School()
school.school_classes.extend([SchoolClass(itm) for itm in s_classes])

tmp = humans[:]
tmp.extend(teachers)
students = [Student(name=random.choice(names), surname=random.choice(surnames), father=random.choice(tmp),
                    mother=random.choice(tmp)) for itm in range(40)]

school.add_teacher(*teachers)
school.add_student(*students)

# 1. Получить полный список всех классов школы
print(f'Полный список всех классов школы: {school.get_classes}')

# 2. Получить список всех учеников в указанном классе
random_class = random.choice(school.school_classes)
print(f'В классе {random_class.name} учатся: \n{random_class.get_students}')

# 3. Получить список всех предметов указанного ученика
random_student = random.choice(students)
print(f'Список предметов ученика {random_student.full_name}: \n{random_student.get_subjects}')

# 4. Узнать ФИО родителей указанного ученика
random_student = random.choice(students)
print(f'ФИО родителей ученика {random_student.full_name}: \n{random_student.get_parents}')

# 5. Получить список всех Учителей, преподающих в указанном классе
random_class = random.choice(school.school_classes)
print(f'В классе {random_class.name} преподают: \n{random_class.get_teachers}')
