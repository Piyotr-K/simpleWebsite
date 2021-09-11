from Employee import Employee

class Programmer(Employee):

    total_programmers = 0

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang
        Programmer.total_programmers += 1
    
    def get_lang(self):
        return self.prog_lang
    
    # def get_fname(self):
    #     return super().first

    # Magic Method
    def __str__(self):
        return f"{super().get_fname()}, {super().get_lname()}, pay: {super().get_pay()}, programming language: {self.prog_lang}"