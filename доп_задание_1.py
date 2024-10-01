grades = [5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]
a = [5,3,3,5,4]
a_sred = sum(a)/len(a)
b = [2,2,2,3]
b_sred = sum(b)/len(b)
c = [4,5,5,2]
c_sred = sum(c)/len(c)
d = [4,4,3]
d_sred = sum(d)/len(d)
e = [5,5,5,4,5]
e_sred = sum(e)/len(e)
sred_ball = (a_sred,b_sred,c_sred,d_sred,e_sred)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
print("Список по алфавиту", students_list)
students_grades = dict(zip(students_list, sred_ball))
print(students_grades)


