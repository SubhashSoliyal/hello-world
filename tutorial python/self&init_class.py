class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole) -> None:
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role} "




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