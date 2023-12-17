class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        #afiseaza nr de angajati
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        #afiseaza detaliile angajatilor
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


#X=PANAIT = 6
#Y=VLAD-MARIAN = 10

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"B03_{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        x = 10 % 3
        if x == 0:
            print(f"Name: {self.name}")
        if x == 1:
            print(f"Salary: {self.salary}")
        if x == 2:
            print(f"Department: {self.department}")

#main.py
#Y/3 = 3.33 => voi crea 4 manageri(rotunjire prin adaos :) )

manager1=Manager("Ionescu Ion", 2200, "Finante")
manager2=Manager("Popescu Ion", 2500, "IT")
manager3=Manager("Enescu Vali", 2400, "")
manager4=Manager("Georgescu George", 3400, "")

#afisez cei 4 manageri(doar salariul)

manager1.display_employee()
manager2.display_employee()
manager3.display_employee()
manager4.display_employee()

#creez 4 obiecte din clasa employee

employee1 = Employee("Enescu George", "2100")
employee2 = Employee("Dobrescu Pop", "2900")
employee3 = Employee("Ionescu Pop", "2700")
employee4 = Employee("Georgescu Ion", "3400")

#afisez 4 obiecte din clasa employee(nume + salariu)

employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
employee4.display_employee()

print(employee1.empCount) #va afisa 8(aduna +1 si la creare in Employee, cat si la creare in Manager, in empCount)
print(manager1.mgr_count)  #va afisa 4(aduna +1 doar la creare in Manager, in mgr_count)


