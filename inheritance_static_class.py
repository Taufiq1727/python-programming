class Employee:
    comapny = "Hp"
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)


    @staticmethod
    def sum(a,b):
        return a+b

    @classmethod
    def print_company(cls):  
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.comapny = new_company
e1 = Employee("Jack", 3455)
e2 = Employee("jill",3466)

e1.print_info()
e2.print_info()
print(e2.sum(5,34))
e1.print_company()
e1.change_company("acer")
e1.print_company()
print(Employee.company)