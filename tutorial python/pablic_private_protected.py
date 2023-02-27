# public 

# protected

# private

class Employee:
    no_of_leaves = 8
    _Protected = 78
    __private = 90

    def __init__(self, aname, asalary, arole) -> None:
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role} "

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    # class methode as a alternative constructor
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    # static methods ii class
    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return "Thanga", 89
    
emp = Employee("harry",7687,"Programmer")
print(emp.no_of_leaves) #public variable
print(emp._Protected)# protected variable
# print(emp.__private)#privare variable
print(emp._Employee__private)#privare variable, done by name randring

    