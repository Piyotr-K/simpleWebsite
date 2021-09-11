from Employee import Employee
from Programmer import Programmer
from Manager import Manager
import random

list_fnames = ["John", "Sam", "Michael", "Piyotr", "Daisy", "Peach", "Ew", "No Girls"]
list_lname = ["McGregor", "St-Pierre", "ImCallingTwitter", "Whatduh", "Cancelled", "54"]
manager_list = []
prog_list = []

for x in range(0, random.randint(3,5)):
    prog_list.append(Programmer(random.choice(list_fnames),
                    random.choice(list_lname),
                    random.randint(300, 700),
                    "Python"))

for x in range(0, random.randint(3,5)):
    manager_list.append(Manager(random.choice(list_fnames),
                    random.choice(list_lname),
                    random.randint(500, 1000),
                    "Marketing"))

print(f'''
Total Employees: {Employee.total_employees}
Total Programmers: {Programmer.total_programmers}
Total Managers: {Manager.total_managers}
''')

# print(isinstance(prog_list[0], Programmer))
# print(issubclass(Programmer, Employee))

print(prog_list[0].get_pay())
prog_list[0] + 50
print(prog_list[0].get_pay())
print(len(prog_list[0]))