"""
@author : Syed Mahvish
CWID : 10456845
"""

import os
from typing import List, Iterator, Tuple, Dict
from datetime import datetime, timedelta
from prettytable import PrettyTable

class ModuleDemo:
    """This class demonstrate use of timedate and typing module."""


    def date_arithmetic(self) -> Tuple[datetime, datetime, int]:
        """This function use Python’s datetime module to calculate date and
        number of days between two dates."""

        date1 : datetime = datetime.strptime("Feb 27, 2020", "%b %d, %Y")
        date2 : datetime = datetime.strptime("Feb 27, 2019", "%b %d, %Y")
        date3 : datetime = datetime.strptime("Feb 01, 2019", "%b %d, %Y")
        date4 : datetime = datetime.strptime("Sep 30, 2019", "%b %d, %Y")

        three_days_after_02272020: datetime = datetime.strftime(date1 +
                                                                timedelta(days=3),"%b %d, %Y")
        three_days_after_02272019: datetime = datetime.strftime(date2 +
                                                                timedelta(days=3),"%b %d, %Y")
        days_passed_02012019_09302019: int = (date4 - date3).days

        return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019

    def read_input(self) -> None:
        """This method reads input for file-reader() and prints output."""

        try:
            path : str  = input("Enter file path: ")
            field : str = input("Enter number of fields in given file: ")
            sep : str = input("Enter separator used in given file(optional): ")
            header : str = input("Is header is included(optional) Y/N: ")

            header_value : bool = False

            if len(sep.strip()) == 0:
                sep = ","
            if header == "Y":
                header_value = True

            for item in self.file_reader(path, field, sep, header_value):
                print(" ".join(item))
                print()

        except Exception as error_value:
            print(f"Error found : {error_value}")

    def file_reader(self, path : str, fields : int, sep : str = ",", header :bool = False) -> Iterator[List[str]]:
        """This function reads file line by line using generator and next
        function And yeilds tuple of str eliminating delimiters."""

        if not isinstance(path, str) or not path or len(path.strip()) == 0:
            raise ValueError("Invalid path")

        fields = int(fields)
        if not isinstance(fields, int) or fields <= 0:
            raise ValueError("Invalid number of field")

        field_array : List[str] = list()
        header_array : List[str] = list()

        try:
            for i,line in enumerate(open(path,"r", encoding="ISO-8859-1")):
                line = line.rstrip("\n")
                field_array = line.split(sep)
                length : int = len(field_array)

                if length < fields or length > fields:
                    raise ValueError(
                        f"ValueError: {path} has {length} fields on line:{i} but expected {fields}")

                if header and i == 0:
                    header_array = line.split(sep)
                else:
                    if len(header_array) > 0:
                        yield [header_name + ': ' + field_name
                                for header_name,field_name  in zip(header_array, field_array)]
                    else:
                        yield field_array
        except FileNotFoundError:
            print(f"Error found : Cannot open/read file : {path}")

class FileAnalyzer:
    """This class demonstrate use of sys module."""


    def __init__(self, directory: str) -> None:
        """This method initialize directory and summary instance."""

        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        if not os.path.isdir(self.directory):
            raise FileNotFoundError(f"Invalid directory path => {self.directory}")

        self.analyze_files()

    def analyze_files(self) -> None:
        """This method reads file from directory that ends with .py And create
        dict of summary."""

        files_list : List[str] = list()

        for root,directory,files in os.walk(self.directory):
            for file in files:
                if '.py' in file:
                    files_list.append(os.path.join(root, file))

        lines_count : int = 0
        character_count : int = 0
        function_count : int = 0
        class_count : int = 0

        for item in files_list:
            lines_count = 0
            character_count = 0
            function_count = 0
            class_count = 0
            data_summary : Dict[str : int] = dict()

            try:
                for line in open(item,"r", encoding="ISO-8859-1"):
                    lines_count += 1
                    character_count += len(line)
                    if "def" in line and line.split()[0] == "def":
                        function_count += 1
                    if "class" in line and line.split()[0] == "class":
                        class_count += 1

                data_summary["classes"] = class_count
                data_summary["functions"] = function_count
                data_summary["lines"] = lines_count
                data_summary["characters"] = character_count
                self.files_summary[item] = data_summary

            except FileNotFoundError:
                print(f"Error found : Cannot open/read file : {item}")

    def pretty_print(self) -> None:
        """This method print file summary in pretty table format."""

        print(f"\nSummary for {self.directory} => \n\n")

        table : PrettyTable = PrettyTable(field_names=
                                            ["File Name" , "Classes",
                                            "Functions" ,"Lines",
                                            "Characters"])
        for key,values in self.files_summary.items():
            table.add_row(
                [key,values["classes"],
                values["functions"],
                values["lines"],
                values["characters"]])
        print(f"{table} \n\n")

def main() -> None:
    """Main method calls function and check output."""
    try:
        module_t = ModuleDemo()
        print(module_t.date_arithmetic())
        module_t.read_input()

        file = FileAnalyzer("/Users/mahvishsyed/Documents/test")
        file.pretty_print()
    except Exception as error_value:
        print(f"Error found in main: {error_value}")

if __name__ == '__main__':
    main()
