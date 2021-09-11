class Employee:

    # This is also another way of creating new class variables
    raise_amount = 1.04 # Float

    total_employees = 0
    
    # Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@companymail.com"
        Employee.total_employees += 1
    
    def get_fname(self):
        return self.first

    def get_lname(self):
        return self.last

    def get_pay(self):
        return self.pay

    # So return is what you get out of using the method
    def fullname(self):
        return f"{self.first} {self.last}" # Here we return a string for using fullname

    def emailAndPay(self):
        return f"Pay: {self.pay}, Email: {self.email}"
    
    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Allows you to just use + sign to add
    def __add__(self, raise_amt):
        self.pay += raise_amt
        print("heeeheeee")
    
    # Allows the use of len() method on the object
    def __len__(self):
        return 500
    
    # cls means class
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # ignores class and instance, there from the beginning
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True