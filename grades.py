student_grades = {}

def add_student(name, grade): 
    student_grades[name] = grade
    print(f'Student {name} added in grade {grade}')

def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f'Student {name} removed')


# Function to display all students and their grades
def display_students():
    print('Students:')
    for name, grade in student_grades.items():
        print(f'{name}, Grade {grade}')

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f'Student {name} was updated to grade {grade}')
    else: 
        print('Student not found')

# Add some students
add_student('zach', 8)
add_student('tim', 3)
add_student('pepe', 4)

# Display students and their grades
display_students()

# Update a student's grade
update_grade('zach', 7)

# Remove a student
remove_student('pepe')

# Display students and their grades again
display_students()