class Employee:
    def __init__(self, name: str):
       self.name = name

class SalaryEmployee(Employee):
    def __init__(self, name: str, salary: float):
       super().__init__(name)
       self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: float):
       super().__init__(name)
       self.hourly_rate = hourly_rate
       self.hours_worked = hours_worked

    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, name: str, salary: float, sales: float, commission_rate: float):
       super().__init__(name, salary)
       self.sales = sales
       self.commission_rate = commission_rate

    def calculate_paycheck(self):
        return super().calculate_paycheck() + (self.sales * self.commission_rate)
