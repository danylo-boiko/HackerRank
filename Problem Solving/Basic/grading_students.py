# https://www.hackerrank.com/challenges/grading/problem
# !/bin/python3

def gradingStudents(grades):
    result = list()
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            if mod5 >= 3:
                grade += (5 - mod5)
        result.append(grade)
    return result


if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))
