class Employee:
    '''
    Employee Class adalah Class untuk membuat object pegawai.
    '''

    # class variable
    raise_amount = 1
    employee_id = 10000 # 10001 => 10002

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.payment = pay

        self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
        Employee.employee_id += 1
        self.id = Employee.employee_id
    
    # regular method
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    # regular method
    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amount)