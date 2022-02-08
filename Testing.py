import unittest
import Personnel
from Classroom import Classroom
from School import School


class PersonnelTestCase(unittest.TestCase):
    def test_person(self):
        a = Personnel.Person(1234, "OD")
        b = Personnel.Person(1234, "Ori Dar")
        self.assertEqual(a, b)  # comparison by ID

    def test_student(self):
        a = Personnel.Student(1234, 'OD', ['OOP', 'Algo 1'])
        a.add_class('Statistics')
        self.assertEqual(3, len(a.subjects))
        self.assertTrue('Statistics' in a.subjects)

    def test_teacher(self):
        a = Personnel.Teacher(4321, 'Shai Aharon', ['OOP'])
        self.assertEqual(0, a.salary)
        a.set_salary(10000)
        a.get_raise(2000)
        self.assertEqual(12000, a.salary)

    def test_principle(self):
        a = Personnel.Teacher(1, "Noam Hazon", ["AI algo"], 13000)
        b = Personnel.Teacher(2, "Gabriel Nivash", ["Algo 1"], 15000)
        c = Personnel.Teacher(1234, "Shai Aharon", ['OOP'], 10000)

        p = Personnel.Principle(5, 'Boaz Ben Moshe', [a, b, c], 20000)
        # p.print_teachers()
        # print(p)
        p.fire_teacher('Shai Aharon')  # I'm sorry Shai, it's nothing personal, just for testing
        # p.print_teachers()
        self.assertEqual(2, len(p.teachers))


class SchoolTestCase(unittest.TestCase):  # includes short test for classroom
    def test_classroom(self):
        a = Personnel.Teacher(1234, "Shai Aharon", ['OOP'], 10000)
        b = Personnel.Teacher(2345, "Gabriel Nivash", ["Algo 1", 'OOP'], 15000)
        s1 = Personnel.Student(1, 'Ori D', ['OOP', 'Algo 1'])
        s2 = Personnel.Student(2, 'Amir S', ['OOP', 'Algo 1'])
        s3 = Personnel.Student(3, 'Daniel R', ['OOP', 'Algo 1'])
        st = [s1, s2]
        c = Classroom('OOP', a, st)
        c.add_student(s3)
        self.assertEqual(3, len(c.students))
        c.sub_teacher(b)
        self.assertEqual('Gabriel Nivash', c.teacher.name)

    def test_school(self):
        a = Personnel.Teacher(1234, "Shai Aharon", ['OOP'], 10000)
        b = Personnel.Teacher(2345, "Gabriel Nivash", ["Algo 1", 'OOP'], 15000)
        p = Personnel.Principle(5, 'Boaz Ben Moshe', [a, b], 20000)
        s1 = Personnel.Student(1, 'Ori D', ['OOP', 'Algo 1'])
        s2 = Personnel.Student(2, 'Amir S', ['OOP', 'Algo 1'])
        s3 = Personnel.Student(3, 'Daniel R', ['OOP', 'Algo 1'])
        c1 = Classroom('OOP', a, [s1, s2])
        c2 = Classroom('Algo 1', b, [s2, s3])

        s = School('My School!', p, 50000)
        s.add_teacher(a)
        s.add_teacher(b)
        s.add_class(c1)
        s.add_class(c2)

        self.assertTrue(s.budget_status() > 0)
        a.get_raise(10000)  # here's your redemption
        self.assertTrue(s.budget_status() < 0)  # blew our budget


if __name__ == '__main__':
    unittest.main()
