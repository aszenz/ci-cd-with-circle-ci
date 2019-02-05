def isNumeric(var):
    return isinstance(var, int) or isinstance(var, float)


def marks_grade(marks):
    """Converts marks to grades
    
    Args:
        marks (int): marks as an int
    Returns:
        grade character
    Raises:
        AssertionError: If type of marks is not int or float
    """
    assert isNumeric(marks), 'Marks not in right format'
    if marks < 40:
        return 'F'
    if marks >= 40 and marks < 50:
        return 'E'
    if marks >= 50 and marks < 60:
        return 'D'
    if marks >= 60 and marks < 70:
        return 'C'
    if marks >= 70 and marks < 80:
        return 'B'
    if marks >= 80 and marks < 90:
        return 'A'
    return 'A+'