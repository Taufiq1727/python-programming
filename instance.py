class Employee:
    company = "ASUS"
    def __init__(self , salary , name , bond , company):
        self.salary = salary
        self.name = name 
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    def get_company(self):
        return self.company


    def get_info(self):
        print(f"The name of the employess is {self.name} . Salary is {self.salary} . The bond is for {self.bond } years")

e1 = Employee(3400,"Jhon",3 , "Tesla")
print(e1.get_company())

print(Employee.company)
