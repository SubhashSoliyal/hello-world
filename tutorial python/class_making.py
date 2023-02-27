class Employee:
    no_of_leaves = 8

harry = Employee()
rohan = Employee()

harry.name = "Herry"
harry.salary = 4550
harry.role = "instructor"

rohan.nama = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(harry.salary)
rohan.no_of_leaves = 9
print(harry.no_of_leaves, rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(rohan.__dict__)

print(Employee.no_of_leaves)
print(Employee.__dict__)