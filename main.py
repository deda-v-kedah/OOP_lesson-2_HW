class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def evaluation(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка st')
    
    def _gpa(self):
        return Lecturer._gpa(self)

    def __str__(self):

        f = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._gpa()}
Курсы в процессе изучения: { ', '.join(self.courses_in_progress) }
Завершенные курсы: { ', '.join(self.finished_courses) }"""

        return f


    def __lt__(self, other):
        if not isinstance(other, Student):
            print("wrong Сlass")
            return
        return self._gpa() < other._gpa()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка rew')
    
    def __str__(self):
        f = f"Имя: {self.name}\nФамилия: {self.surname}"
        return f

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _gpa(self):
        summ = 0
        i = 0
        for key, value in self.grades.items():
            for grade in value:
                i += 1
                summ += grade
        return summ / i


    def __str__(self):
        f = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._gpa()}"
        return f
 
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("wrong Сlass")
            return
        return self._gpa() < other._gpa()


student1 = Student("Вася", "Васильев", "М")
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student("Петя", "Петров", "М")
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование', 'Англиский для программистов']



reviewer1 = Reviewer("Оксана", "Петрова")
reviewer1.courses_attached += ['Python','Git']
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Git", 5)
reviewer1.rate_hw(student2, "Python", 9)
reviewer1.rate_hw(student2, "Git", 8)

reviewer2 = Reviewer("Оксана", "Петрова")
reviewer2.courses_attached += ['Python','Git']
reviewer2.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student1, "Git", 9)
reviewer2.rate_hw(student2, "Python", 10)
reviewer2.rate_hw(student2, "Git", 9)



lecturer1 = Lecturer("Геннадий", "Болобанов")
lecturer1.courses_attached += ['Python', "Git"]

lecturer2 = Lecturer("Вася", "Рогов")
lecturer2.courses_attached += ['Python', "Git"]

student1.evaluation(lecturer1, "Python", 10)
student2.evaluation(lecturer1, "Python", 10)

student1.evaluation(lecturer2, "Python", 7)
student2.evaluation(lecturer2, "Python", 8)

student1.evaluation(lecturer1, "Git", 8)
student2.evaluation(lecturer1, "Git", 4)

student1.evaluation(lecturer2, "Git", 10)
student2.evaluation(lecturer2, "Git", 8)

print(student1)
print(student2)
print(student1 > student2)

print(lecturer1)
print(lecturer2)
print(lecturer1 < lecturer2)


student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

def gpa(list, curse):
    if isinstance(list[1], Lecturer):
        str = "Cредняя оценка за лекции всех лекторов в рамках курса:"
    elif isinstance(list[1], Student):
        str = "Cредняя оценка за домашние задания по всем студентам в рамках курса:"
    summ = 0
    i = 0
    for el in list:
        summ += sum(el.grades[curse])
        i += len(el.grades[curse])

    print(f"{str} {curse} ровна: {summ / i}")

gpa(student_list, 'Git')
gpa(lecturer_list, 'Python')
    