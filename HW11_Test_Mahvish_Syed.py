"""@author : Syed Mahvish
CWID : 10456845"""

import unittest
from HW11_Mahvish_Syed import StudentReport


class StudentReportTest(unittest.TestCase):
    """This class test Student Report class methods."""

    def test_read_major_file(self) -> None:
        """This method test major data."""
        student = StudentReport()
        student.read_major_file("majors.txt")

        test_major_summary = {'SFEN': {'required_courses': ['SSW 540',
                                                            'SSW 810',
                                                            'SSW 555'],
                                       'elective_courses': ['CS 501',
                                                            'CS 546']},
                              'CS': {'required_courses': ['CS 570',
                                                          'CS 546'],
                                     'elective_courses': ['SSW 810',
                                                          'SSW 565']}}
        self.assertDictEqual(student.major_summary, test_major_summary)

    def test_read_instructor_file(self) -> None:
        """This file test instructor data."""
        student = StudentReport()
        student.read_instructor_file("grades.txt", "instructor.txt")

        test_instructor_summary = {'SSW 810': {'count': 4,
                                               '98763': {'instructor_name': 'Rowland, J',
                                                         'dept': 'SFEN'}},
                                   'CS 501': {'count': 1,
                                              '98762': {'instructor_name': 'Hawking, S',
                                                        'dept': 'CS'}},
                                   'CS 546': {'count': 1, '98762': {'instructor_name': 'Hawking, S',
                                                                    'dept': 'CS'},
                                              '98764': {'instructor_name': 'Cohen, R',
                                                        'dept': 'SFEN'}},
                                   'SSW 555': {'count': 1, '98763': {'instructor_name': 'Rowland, J',
                                                                     'dept': 'SFEN'}},
                                   'CS 570': {'count': 1, '98762': {'instructor_name': 'Hawking, S',
                                                                    'dept': 'CS'}}}
        self.assertDictEqual(student.instructor_summary, test_instructor_summary)

    def test_student_grades_table_db(self) -> None:
        """This file test student_grades_table_db data."""

        student = StudentReport()
        student.student_grades_table_db("HW11_DB_File")
        db_output = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                     ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                     ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                     ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                     ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                     ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                     ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                     ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                     ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]

        self.assertEqual(student.row_list, db_output)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
