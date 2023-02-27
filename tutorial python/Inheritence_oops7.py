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
    
    #Abstrection and Encapsulation in class or oops


# Inheritence 

class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole,languages) -> None:
        super().__init__(aname, asalary, arole)
        self.languages = languages

    def printProg(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.languages} "
    

# Multiple Inheritence 

class Player:
    no_of_game = 4
    def __init__(self, name, game) -> None:
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name}. Game is {self.game} "


class CoolProgrammer(Employee, Player):
    language = "c++"
    def printLanguage(self):
        print(self.language)
        
    



harry = Employee("Harry", 5000, "Instructor")
rohan = Employee("Rohan", 4000, "student")
# karan = Employee.from_dash("Karan-4800-student")

# shubham = Programmer('Subham', 7000, "Programmer",["Python"])
# karan = Programmer("Karan", 8000, "Programmer",["python", "C++"])
# print(karan.printProg())
# print(karan.printdetails())
# print(karan.no_of_holiday)

subhash = Player("Subhash", ["Cricet"])
soliyal = CoolProgrammer("Soliyal", 100000, "CoolProgrammer")
det = soliyal.printdetails()
soliyal.printLanguage()
print(det)

