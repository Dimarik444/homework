grades = [5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]
sred_ball = sum(grades)/len(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
print("Список по алфавиту", students_list)
students_grades = dict(zip(students_list, grades))
print(students_grades)


