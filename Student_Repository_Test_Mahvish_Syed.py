"""@author : Syed Mahvish
CWID : 10456845"""

import unittest
from HW08_Mahvish_Syed import FileAnalyzer, ModuleDemo

class ModuleDemoTest(unittest.TestCase):
    """This class test Module Demo class methods."""


    def test_date_arithmetic(self) -> None:
        """This method test date_arithmetic()"""
        module_obj = ModuleDemo()

        self.assertEqual(module_obj.date_arithmetic(),('Mar 01, 2020', 'Mar 02, 2019', 241))
        self.assertNotEqual(module_obj.date_arithmetic(),('Mar 01, 2020', 'Mar 02, 2020', 241))
        self.assertNotEqual(module_obj.date_arithmetic(),('Mar 01, 2019', 'Mar 02, 2020', 241))
        self.assertNotEqual(module_obj.date_arithmetic(),('Mar 01, 2019', 'Mar 02, 2020', 2))

    def test_file_reader(self) -> None:
        """This method test file_reader() method."""
        module_obj = ModuleDemo()

        file1 = module_obj.file_reader("header.txt",4,"|", True)
        file2 = module_obj.file_reader("example.txt",3,"|",False)

        self.assertEqual(next(file1),['CWID: 123', 'Name: Mahvish', 'Major: CS', 'Age: 23'])
        self.assertEqual(next(file1),['CWID: 24', 'Name: Shweta', 'Major: MS', 'Age: 25'])
        self.assertEqual(next(file1),['CWID: 134', 'Name: Priya', 'Major: CS', 'Age: 24'])

        self.assertEqual(next(file2),['123', 'Mahvish', 'CS'])
        self.assertEqual(next(file2),['24', 'Shweta', 'MS'])
        self.assertNotEqual(next(file2),['3445', 'Shweta', 'SSW'])

class FileAnalyzerTest(unittest.TestCase):
    """This class test file analyser class and its methods."""


    def test_init(self) -> None:
        """This method test init() method of FileAnalyzer."""

        self.assertRaises(FileNotFoundError,FileAnalyzer,"notDirectory.txt")

    def test_analyze_files(self) -> None:
        """This method test analyze_files() method of FileAnalyser."""
        fileanalyser_obj = FileAnalyzer("/Users/mahvishsyed/Documents/test")
        test_dict = {'/Users/mahvishsyed/Documents/test/0_defs_in_this_file.py':
                        {'classes': 0, 'functions': 0, 'lines': 3, 'characters': 57},
                    '/Users/mahvishsyed/Documents/test/file1.py':
                        {'classes': 2, 'functions': 4, 'lines': 25, 'characters': 270}}
        self.assertDictEqual(fileanalyser_obj.files_summary,test_dict)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
