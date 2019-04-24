class Human:
    def __init__(self, human_data):
        human_data = human_data.split()
        self.name = human_data[1]
        self.patronymic = human_data[2]
        self.surname = human_data[0]

    def get_full_name(self):
        return '{} {} {}'.format(self.name, self.patronymic, self.surname)

class Class_room:
    def __init__(self, class_name, subjects):
        self.class_name = {'class_num': int(class_name.split()[0]),
                           'class_char': class_name.split()[1]}
        self.subjects = subjects

    def main_class_name(self):
        p_class = '{} {}'. format(self.class_name['class_num'], self.class_name['class_char'])
        return p_class

    def class_subjects(self):
        message = 'Ученик {} {} класса изучает {}'.format(self.get_full_name(), self.main_class_name(), self.subjects)
        return message

class Parents:
    def __init__(self, dad_name, mom_name):
        self.dad_name = dad_name
        self.mom_name = mom_name

    def parents_name(self):
        p_name = 'Отец: {} \nМать: {}'.format(self.dad_name, self.mom_name)
        return p_name

class Pupil(Human, Parents, Class_room):
    def __init__(self, human_data, class_name, subjects, dad_name, mom_name):
        Human.__init__(self, human_data)
        Parents.__init__(self, dad_name, mom_name)
        Class_room.__init__(self, class_name, subjects)


class Teacher(Human):
    def __init__(self, human_data, teach_classes, subject):
        Human.__init__(self, human_data)
        self.teach_classes = teach_classes
        self.subject = subject


    def classes(self):
        return 'Учитель: {} \nпредмет: {} \nклассы: {}'.format(self.get_full_name(), self.subject, self.class_name)

subjects_7a = ['математика', 'английский', 'физика']
subjects_7b = subjects_7a
subjects_8v = ['физика', 'химия', 'геометрия', 'обществознание']
pupil_1 = Pupil('Достоевский Сергей Федорович', '7 A', subjects_7a, 'Федор Михайлович Достоевский', 'Анна Андреевна Ахматова')
pupil_2 = Pupil('Грозный Дмитрий Иванович', '7 A', subjects_7a, 'Иоанн Васильевич Грозный', 'Марфа Васильевна Собакина')

parent_1 = Parents('Федор Михайлович Достоевский', 'Анна Андреевна Ахматова')

teacher_1 = Teacher('Перельман Яков Исидорович', ['7 A','7 Б','8 В'], 'физика')
teacher_2 = Teacher('Менделеев Дмитрий Иванович', ['8 A', '8 B'], 'химия')
print(pupil_1.parents_name())
print(teacher_1.subject)
