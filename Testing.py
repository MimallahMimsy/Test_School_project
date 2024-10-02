from Human import Human
from Student import Student
from Teacher import Teacher
from Class import Class
from Subject import Subject
import unittest


class TestSchool(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Ахмед", "Васильевич")
        self.student2 = Student("Борис", "Васильевич")
        self.student3 = Student("Борис", "Борисыч")
        self.student4 = Student("Денис", "Георгиевич")
        self.student5 = Student("Георгий", "Денисович")
        self.classroom_teacher = Teacher("Иван", "Иванов", [Subject.MATH, Subject.RUSSIAN_LANG])
        self.school_class = Class(10, "A", self.classroom_teacher, [self.student1])

    def test_set_class(self):
        self.student2.set_class(self.school_class)
        self.student3.set_class(self.school_class)
        self.student4.set_class(self.school_class)
        self.student5.set_class(self.school_class)
        self.assertEqual(self.student1.get_class(), self.school_class)  # для школьника, что при создании класса с передачей школьника, школьнику также устанавливается данный класс
        self.assertEqual(self.student2.get_class(), self.school_class)  # для школьника, что set_class устанавливает класс
        self.assertIn(self.student2, self.school_class._students) # для класса, что при set_class школьник передается в список студентов класса
        self.classroom_teacher.set_class(self.school_class)
        self.assertEqual(self.classroom_teacher.get_class(), self.school_class)  # для учителя set_class

    def test_getitem(self):
        self.student2.set_class(self.school_class)
        self.student3.set_class(self.school_class)
        self.student4.set_class(self.school_class)
        self.student5.set_class(self.school_class)
        self.assertEqual(self.school_class['Г'], [self.student4, self.student5])  # Ищем школьников на Г
    def test_lt(self):
        self.assertTrue(self.student1 < self.student2) #сравниваем школьников
    def test_csv_writer_and_reader(self):
        self.student2.set_class(self.school_class)
        self.student3.set_class(self.school_class)
        self.student4.set_class(self.school_class)
        self.student5.set_class(self.school_class)
        self.school_class.csv_writer()
        saved_class=Class.csv_reader()
        self.assertEqual(saved_class._grade, "10")
        self.assertEqual(saved_class._letter, "A")
        self.assertEqual(len(saved_class), len(self.school_class))
        self.assertEqual(saved_class._homeroom_teacher._name, self.classroom_teacher._name)
        self.assertEqual(saved_class._homeroom_teacher._subjects, self.classroom_teacher._subjects)

