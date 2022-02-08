import unittest
import Personnel


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


me = Personnel.Person(212458244, 'Ori Darshan')
print(me)
a = Personnel.Teacher(1234, "Noam Hazon", ["AI algo"], 15000)
b = Personnel.Teacher(1234, "OR", ["AI2 algo"], 15000)
c = Personnel.Teacher(1234, "oam Hazon", ["AI3 algo"], 15000)
x = [a,b,c]
print(x)

if __name__ == '__main__':
    unittest.main()
