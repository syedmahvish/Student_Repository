"""
@author : Syed Mahvish
CWID : 10456845
"""

from typing import List, Iterator, Dict
from prettytable import PrettyTable

REQUIRED_COURSES = "required_courses"
ELECTIVE_COURSES = "elective_courses"
INSTRUCTOR_NAME = "instructor_name"
DEPARTMENT = "dept"
STUDENT_COUNT = "count"
NAME = "name"
MAJOR = "major"
COMPLETED_COURSE = "completed_courses"
REMAINING_COURSE = "remaining_courses"
REMAINING_ELECTIVE = "remaining_elective"


class StudentReport:
    """This class prints prettytable for Student Majors, Instructor information
    and Courses need to complete graduation."""

    def __init__(self) -> None:
        """This method initialize dictionary to maintain information."""
        self.major_summary: Dict[str, Dict[str, List[str]]] = dict()
        self.student_summary: Dict[str, Dict[str, any]] = dict()
        self.instructor_summary: Dict[str, Dict[str, any]] = dict()
        self.complete_course: Dict[str, List[str]] = dict()

    def file_reader(self, path: str,
                    fields: int,
                    sep: str = ",",
                    header: bool = False) -> Iterator[List[str]]:
        """This function reads file line by line using generator and next
        function And yeilds tuple of str eliminating delimiters."""

        if not isinstance(path, str) or not path or len(path.strip()) == 0:
            raise ValueError("Invalid path")

        fields = int(fields)
        if not isinstance(fields, int) or fields <= 0:
            raise ValueError("Invalid number of field")

        field_array: List[str] = list()

        try:
            with open(path) as file_name:
                for i, line in enumerate(file_name):
                    line = line.rstrip("\n")
                    field_array = line.split(sep)
                    length: int = len(field_array)

                    if length != fields:
                        raise ValueError(
                            f"Error: {path} has {length} fields on line:{i} but expected:{fields}")

                    if header and i == 0:
                        continue
                    else:
                        yield field_array
        except FileNotFoundError:
            print(f"Error found : Cannot open/read file : {path}")

    def read_major_file(self, path) -> None:
        """This function reads and create dictionary for major file."""

        for major, req_or_elec, course in self.file_reader(path, 3, "\t", True):
            temp_dict: Dict[str, List[str]] = dict()
            temp_dict[REQUIRED_COURSES]: List[str] = list()
            temp_dict[ELECTIVE_COURSES]: List[str] = list()

            if major in self.major_summary.keys():
                temp_dict = self.major_summary[major]

            if req_or_elec == "R":
                temp_dict[REQUIRED_COURSES].append(course)
            elif req_or_elec == "E":
                temp_dict[ELECTIVE_COURSES].append(course)
            else:
                raise ValueError(f"Course : {course} is neither requrired nor elective")

            self.major_summary[major] = temp_dict

        table: PrettyTable = PrettyTable(field_names=["Majors",
                                                      "Required Courses",
                                                      "Elective"])

        for key, values in self.major_summary.items():
            table.add_row(
                [key,
                 values[REQUIRED_COURSES],
                 values[ELECTIVE_COURSES]])
        print("\nMajors Summary\n")
        print(f"{table} \n\n")

    def read_instructor_file(self, grade_file_path: str, instructor_file_path: str) -> None:
        """This function reads grade and instructor file and display
        instructor,course and student count detials."""

        temp_instructor_dict: Dict[str: Dict[str: str]] = dict()
        table: PrettyTable = PrettyTable()

        for instructor_id, name, dept in self.file_reader(
                instructor_file_path, 3, "|", True):
            temp_dict: Dict[str, str] = dict()
            if instructor_id not in temp_instructor_dict:
                temp_dict[INSTRUCTOR_NAME] = name
                temp_dict[DEPARTMENT] = dept

            temp_instructor_dict[instructor_id] = temp_dict

        for student_id, course, grades, instructor_id in self.file_reader(grade_file_path, 4,
                                                                          "|", True):
            temp_dict: Dict[str, int] = dict()
            temp_dict[STUDENT_COUNT]: int = 0

            if course in self.instructor_summary.keys():
                temp_dict = self.instructor_summary[course]

            if instructor_id in temp_instructor_dict.keys():
                temp_dict[instructor_id] = temp_instructor_dict[instructor_id]

            if grades in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
                if student_id in self.complete_course.keys():
                    self.complete_course[student_id].append(course)
                else:
                    self.complete_course[student_id] = [course]

            temp_dict[STUDENT_COUNT] = temp_dict[STUDENT_COUNT] + 1

            self.instructor_summary[course] = temp_dict

            table = PrettyTable(field_names=["CWID",
                                             "Name",
                                             "Dept",
                                             "Course",
                                             "Students"])

            for key, values in self.instructor_summary.items():
                for item_key, item_value in values.items():
                    if item_key != STUDENT_COUNT:
                        table.add_row([item_key, item_value[INSTRUCTOR_NAME],
                                       item_value[DEPARTMENT], key, values[STUDENT_COUNT]])

        print("\nInstructor Summary\n")
        print(f"{table} \n\n")

    def read_student_file(self, path: str) -> None:
        """This function reads student file and prints student details with
        completed and remaining courses."""

        for student_id, name, major in self.file_reader(path, 3, ";", True):
            temp_dict: Dict[str, int] = dict()
            all_courses: List[str] = list()
            all_elective: List[str] = list()
            completed_course_list: List[str] = list()

            if major in self.major_summary.keys():
                temp_major_dict: Dict[str, List[str]] = self.major_summary[major]
                all_courses = temp_major_dict[REQUIRED_COURSES]
                all_elective = temp_major_dict[ELECTIVE_COURSES]

            if student_id in self.student_summary.keys():
                temp_dict = self.student_summary[student_id]

            temp_dict[NAME] = name
            temp_dict[MAJOR] = major

            if student_id in self.complete_course.keys():
                completed_course_list = self.complete_course[student_id]

            temp_dict[COMPLETED_COURSE] = completed_course_list

            remaining_courses: List[str] = list(set(all_courses)
                                                .difference(set(completed_course_list)))
            temp_dict[REMAINING_COURSE] = remaining_courses

            remaining_courses = list(set(all_elective).intersection(set(completed_course_list)))
            if len(remaining_courses) == 0:
                remaining_courses = list((set(all_elective).difference(set(completed_course_list)))
                                         .difference(set(all_courses)))
            else:
                remaining_courses = []
            temp_dict[REMAINING_ELECTIVE] = remaining_courses

            self.student_summary[student_id] = temp_dict

        table: PrettyTable = PrettyTable(field_names=["CWID", "Name", "Major",
                                                      "Completed Course", "Remaining Course",
                                                      "Remaining Elective"])

        for key, values in self.student_summary.items():
            table.add_row([key, values[NAME],
                           values[MAJOR], values[COMPLETED_COURSE],
                           values[REMAINING_COURSE], values[REMAINING_ELECTIVE]])

        print("\nStudent Summary\n")
        print(f"{table} \n\n")

    def read_input(self) -> None:
        """This method reads input for file-reader()"""

        try:
            major_path: str = input("Enter Major file path: ")
            grade_path: str = input("Enter Grade file path: ")
            instructor_path: str = input("Enter Instructor file path: ")
            student_path: str = input("Enter Student file path: ")

            self.read_major_file(major_path)
            self.read_instructor_file(grade_path, instructor_path)
            self.read_student_file(student_path)
        except Exception as error_value:
            print(f"Error found in reading input: {error_value}")


def main() -> None:
    """Main method calls function and check output."""
    try:
        student = StudentReport()
        student.read_input()
    except Exception as error_value:
        print(f"Error found in main: {error_value}")


if __name__ == '__main__':
    main()
