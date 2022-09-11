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
            print('Ошибка')
    
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
            print('Ошибка')
    
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
student1.courses_in_progress += ['Python', 'git']
student1.finished_courses += ['Введение в программирование']

student2 = Student("Петя", "Петров", "М")
student2.courses_in_progress += ['Python']

student3 = Student("Федр", "Рогов", "М")
student3.courses_in_progress += ['Git']


student4 = Student("Саша", "Михеев", "М")
student4.courses_in_progress += ['Python', "Git"]


reviewer = Reviewer("Оксана", "Петрова")

reviewer.courses_attached += ['Python','git']

reviewer.rate_hw(student1, "Python", 10)
reviewer.rate_hw(student1, "git", 5)
reviewer.rate_hw(student2, "Python", 10)

lecturer1 = Lecturer("Геннадий", "Болобанов")
lecturer1.courses_attached += ['Python', "Git"]

lecturer2 = Lecturer("Вася", "Рогов")
lecturer2.courses_attached += ['Python', "Git"]

student1.evaluation(lecturer2, "Python", 1)
student2.evaluation(lecturer2, "Python", 1)
student3.evaluation(lecturer2, "Git", 1)
student4.evaluation(lecturer2, "Python", 1)
student4.evaluation(lecturer2, "Git", 1)

student1.evaluation(lecturer1, "Python", 10)
student2.evaluation(lecturer1, "Python", 10)
student3.evaluation(lecturer1, "Git", 10)
student4.evaluation(lecturer1, "Python", 10)
student4.evaluation(lecturer1, "Git", 10)

# print(student1.grades)
# print(student2.grades)

# print(lecturer.grades)

# print(reviewer)
print(lecturer1)
print(lecturer2)

# print(student1)

print( lecturer1 < lecturer2 )

print(student1 < student2)