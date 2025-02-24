class Employee:
    company = "ITC"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
        
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Alice", 50000)
b = Programmer("Bob", 60000, "Python")


print(a.company, b.company)


a.show()
b.showLanguage()









# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the Employee is{self.name} and the salary is {self.salary} ")

# class Programmer(Employee):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

#     a = Employee()
#     b = Programmer()

#     print(a.company,b.company)                