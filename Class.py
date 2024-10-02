from Student import Student
from Teacher import Teacher
from typing import List
import csv
import re
from Subject import Subject

class Class(List):
    def __init__(self, grade, letter, homeroom_teacher, students=None):
        self._homeroom_teacher = homeroom_teacher
        self._students = students
        self._letter = letter
        self._grade = grade
        if self._students is not None:
            for student in self._students:
                student._class = self
        else:
            self._students = []

    def __iter__(self):
        sorted_st = sorted(self._students, key=lambda _students: (_students._lastname, _students._name))
        return iter(sorted_st)

    def __getitem__(self, name):
        found_st = []
        for student in self._students:
            if name in student._name or name in student._lastname:
                # print('Найден школьник:', student._name, student._lastname)
                found_st.append(student)
        return found_st

    def __str__(self):
        return (
            f"Класс: {self._grade}{self._letter}, Классный руководитель: {self._homeroom_teacher._name} {self._homeroom_teacher._lastname}")

    def __repr__(self):
        return f"class: grade={self._grade}, letter='{self._letter}', homeroom_teacher={self._homeroom_teacher._name} {self._homeroom_teacher._lastname}"

    def csv_writer(self):
        print('Введите имя файла для сохранения')
        filename = input()
        with open(filename + '.csv', mode='w', newline='', encoding='utf-8') as file:
            csvwriter = csv.writer(file)
            for student in self._students:
                csvwriter.writerow(
                    [self._grade, self._letter, student._name, student._lastname, self._homeroom_teacher._name,
                     self._homeroom_teacher._lastname, ','.join(
                        subject.value for subject in self._homeroom_teacher._subjects)])

    @staticmethod
    def csv_reader():
        print('Введите имя считываемого файла')
        filename = input()
        students = []

        with open(filename + '.csv', mode='r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                grade, letter, name, lastname, teacher_name, teacher_lastname, subjects = row[0], row[1], row[2], row[
                    3], row[4], row[5], row[6]
                student = Student(name, lastname)
                result = re.split(',', subjects)
                teacher = Teacher(teacher_name, teacher_lastname, [Subject(sub.strip()) for sub in result])
                students.append(student)
            class_read = Class(grade, letter, teacher, students)
            return class_read
