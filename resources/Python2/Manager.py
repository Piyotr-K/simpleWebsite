from Employee import Employee

class Manager(Employee):

    total_managers = 0

    def __init__(self, fname, lname, pay, team):
        super().__init__(fname, lname, pay)
        self.team = team
        Manager.total_managers += 1
    
    def get_team(self):
        return self.team