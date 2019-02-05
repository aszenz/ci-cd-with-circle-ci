from marks_grader import marks_grade

assert marks_grade(28) == 'F'
assert marks_grade(45) == 'E'
assert marks_grade(58) == 'D'
assert marks_grade(65) == 'C'
assert marks_grade(75) == 'B'
assert marks_grade(82) == 'A'
assert marks_grade(95) == 'A+'
