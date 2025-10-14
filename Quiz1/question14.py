def grouping(grades: list):
    sorted_grades = {
        'A' : [],
        'B' : [],
        'C' : []
    }
    for grade in grades:
        if grade > 17:
            sorted_grades['A'].append(grade)
        elif 12 <= grade < 17:
            sorted_grades['B'].append(grade)
        else:
            sorted_grades['C'].append(grade)
    return sorted_grades
grades = list(map(int, input("Please enter the grades :").split()))
result = grouping(grades)
print(result)