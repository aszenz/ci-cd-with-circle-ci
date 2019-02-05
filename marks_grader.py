def isNumeric(var):
    return isinstance(var, int) or isinstance(var, float)


def marks_grade(marks):
    assert (isNumeric(marks), 'Marks not in right format')
    if marks < 40:
        return 'F'
    elif marks >= 40 and marks < 50:
        return 'E'
    elif marks >= 50 and marks < 60:
        return 'D'
    elif marks >= 60 and marks < 70:
        return 'C'
    elif marks >= 70 and marks < 80:
        return 'B'
    elif marks >= 80 and marks < 90:
        return 'A'
    return 'A+'