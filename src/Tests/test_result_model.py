# File to test result model
import pytest

from Controllers.html_checker import HtmlChecker

EXISTS_HTML = ""
NOT_EXISTS_HTML = ""

with open("src/Tests/Sources/exist.html") as ex:
    exString = ex.read()
    EXISTS_HTML += exString

with open("src/Tests/Sources/not_exist.html") as nex:
    nexString = nex.read()
    NOT_EXISTS_HTML += nexString


def test_result_model():
    existHtml = HtmlChecker(exString)
    existHtml.find_tables()
    tableExist = existHtml.rmObjects
    assert len(tableExist) == 10, f"10 Subjects expected, {len(tableExist)} returned"
    grades = [x.grade for x in tableExist]
    assert (
        None not in grades
    ), f"All grades are supposed to be not None, but None was found in grades"
    marks = [x.mark for x in tableExist]
    assert (
        None not in marks
    ), f"All marks are supposed to be not None, but None was found in marks"
    notExistHtml = HtmlChecker(nexString)
    notExistHtml.find_tables()
    notTableExist = notExistHtml.rmObjects
    assert len(notTableExist) == 10, f"10 Subjects expected, {len(tableExist)} returned"
    grades = [x.grade for x in notTableExist]
    assert (
        grades.count(None) == 2
    ), f"2 subjects with None expected, {grades.count(None)} returned"
    marks = [x.mark for x in notTableExist]
    assert (
        marks.count(None) == 2
    ), f"2 subjects with None expected, {grades.count(None)} returned"
