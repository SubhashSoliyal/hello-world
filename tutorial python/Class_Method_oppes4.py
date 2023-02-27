class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole) -> None:
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role} "

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves





harry = Employee("Harry", 5000, "Instructor")
rohan = Employee("Rohan", 4000, "student")

# harry.name = "Herry"
# harry.salary = 4550
# harry.role = "instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student" 

print(rohan.printdetails())
print(harry.printdetails())
print(harry.salary)
print(harry.no_of_leaves)

harry.change_leaves(34)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)


