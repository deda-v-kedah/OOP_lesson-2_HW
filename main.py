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


class Lecturer(Mentor):
    grades = {}
    
 
student1 = Student("Вася", "Васильев", "М")
student1.courses_in_progress += ['Python']

student2 = Student("Петя", "Петров", "М")
student2.courses_in_progress += ['Python']

reviewer = Reviewer("Оксана", "Петрова")

reviewer.courses_attached += ['Python']

reviewer.rate_hw(student1, "Python", 10)
reviewer.rate_hw(student2, "Python", 10)

lecturer = Lecturer("Геннадий", "Болобанов")
lecturer.courses_attached += ['Python']

student1.evaluation(lecturer, "Python", 10)
student2.evaluation(lecturer, "Python", 9)
print(student1.grades)
print(student2.grades)

print(lecturer.grades)