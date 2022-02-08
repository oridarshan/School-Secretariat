import Personnel


class Classroom:
    def __init__(self, subject: str, teacher: Personnel.Teacher = None, students: list[Personnel.Student] = None):
        self.subject = subject
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Personnel.Student):
        if self.students:
            self.students.append(student)
        else:
            self.students = [student]

    def sub_teacher(self, sub_teacher: Personnel.Teacher):
        self.teacher = sub_teacher
