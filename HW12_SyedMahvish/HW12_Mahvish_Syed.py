"""
@author : Syed Mahvish
CWID : 10456845

This program is about displaying student data on html page
Using sqlite for database
"""

import sqlite3
from typing import Dict
from flask import Flask, render_template

app: Flask = Flask(__name__)

DB_PATH: str = "HW11_DB_file"


@app.route("/student_result")
def student_grades_table_db() -> str:
    """ This method execute db sql query
        and print result using flask"""

    db_connect: sqlite3.Connection = sqlite3.connect(DB_PATH)
    query: str = """select s.Name, s.CWID, g.Course, g.Grade, i.Name
                        from grades g join instructor i on g.InstructorCWID = i.CWID
                        join students s on g.StudentCWID = s.CWID
                        order by s.Name"""

    data: Dict[str: str] = \
        [{"Student": stu_name, "CWID": cwid, "Course": course, "Grade": grade, "Instructor": inst_name}
         for stu_name, cwid, course, grade, inst_name in db_connect.execute(query)]

    db_connect.close()

    return render_template("students.html",
                           title="Stevens Repository",
                           table_title="Student,Course,Grade and Instructor",
                           student_table=data)


app.run(debug=True)
