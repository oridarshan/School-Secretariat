import unittest
import Personnel


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



if __name__ == '__main__':
    unittest.main()
