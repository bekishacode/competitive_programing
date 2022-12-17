def gradingStudents(grades):
    # Write your code here
    result =[]
    for grade in grades:
        if grade >= 38:
            remainder = grade % 5
            if remainder >=3:
                grade += 5 - remainder
        result.append(grade)
    return result
