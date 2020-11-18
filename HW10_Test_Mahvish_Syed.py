"""@author : Syed Mahvish
CWID : 10456845"""

import unittest
from HW10_Mahvish_Syed import StudentReport


class StudentReportTest(unittest.TestCase):
    """This class test Student Report class methods."""

    def test_read_major_file(self) -> None:
        """This method test major data."""
        student = StudentReport()
        student.read_major_file("majors.txt")

        test_major_summary = {'SFEN': {'required_courses': ['SSW 540', 'SSW 564',
                                                            'SSW 555', 'SSW 567'],
                                       'elective_courses': ['CS 501', 'CS 513',
                                                            'CS 545']},
                              'SYEN': {'required_courses': ['SYS 671', 'SYS 612',
                                                            'SYS 800'],
                                       'elective_courses': ['SSW 810', 'SSW 565',
                                                            'SSW 540']}}
        self.assertDictEqual(student.major_summary, test_major_summary)

    def test_read_instructor_file(self) -> None:
        """This file test instructor data."""
        student = StudentReport()
        student.read_instructor_file("grades.txt", "instructor.txt")

        test_instructor_summary = {'SSW 567': {'count': 4,
                                               '98765':
                                                   {'instructor_name': 'Einstein, A',
                                                    'dept': 'SFEN'}},
                                   'SSW 564': {'count': 3,
                                               '98764':
                                                   {'instructor_name': 'Feynman, R',
                                                    'dept': 'SFEN'}},
                                   'SSW 687': {'count': 3,
                                               '98764':
                                                   {'instructor_name': 'Feynman, R',
                                                    'dept': 'SFEN'}},
                                   'CS 501': {'count': 1,
                                              '98764':
                                                  {'instructor_name': 'Feynman, R',
                                                   'dept': 'SFEN'}},
                                   'CS 545': {'count': 1,
                                              '98764':
                                                  {'instructor_name': 'Feynman, R',
                                                   'dept': 'SFEN'}},
                                   'SSW 555': {'count': 1,
                                               '98763':
                                                   {'instructor_name': 'Newton, I',
                                                    'dept': 'SFEN'}},
                                   'SSW 689': {'count': 1,
                                               '98763':
                                                   {'instructor_name': 'Newton, I',
                                                    'dept': 'SFEN'}},
                                   'SSW 540': {'count': 3,
                                               '98765':
                                                   {'instructor_name': 'Einstein, A',
                                                    'dept': 'SFEN'}},
                                   'SYS 800': {'count': 1,
                                               '98760': {'instructor_name': 'Darwin, C',
                                                         'dept': 'SYEN'}},
                                   'SYS 750': {'count': 1,
                                               '98760': {'instructor_name': 'Darwin, C',
                                                         'dept': 'SYEN'}},
                                   'SYS 611': {'count': 2,
                                               '98760': {'instructor_name': 'Darwin, C',
                                                         'dept': 'SYEN'}},
                                   'SYS 645': {'count': 1,
                                               '98760': {'instructor_name': 'Darwin, C',
                                                         'dept': 'SYEN'}}}
        self.assertDictEqual(student.instructor_summary, test_instructor_summary)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
