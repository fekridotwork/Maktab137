def student_sort(students: dict):
    '''
    At first we will sort by name and then this would help us in the second sort by 
    grade when 2 grades will be equal
    
    '''
    students.sort(key = lambda x : x['name'])
    students.sort(key = lambda x : x['grade'], reverse = True)

    return students # This sort method is inplace
students = [
{"name": "Reza", "grade": 17},
{"name": "Sara", "grade": 19},
{"name": "Ali", "grade": 17},
{"name": "Mina", "grade": 20}
]
result = student_sort(students)
print(result)