from habit_tracker.employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee
import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

def main():
    company = Company("Tech Solutions")
    employee1 = SalaryEmployee("Alice", 52000)
    employee2 = SalaryEmployee("Bob", 48000)
    employee3 = HourlyEmployee("Charlie", 20.0, 40.0)
    employee4 = CommissionEmployee("Diana",30000, 10000.0, 0.1)

    company.add_employee(employee1)
    company.add_employee(employee2)
    company.add_employee(employee3)
    company.add_employee(employee4)

    for emp in company.employees:
        paycheck = emp.calculate_paycheck()
        logger.info(f"{emp.name} receives a paycheck of ${paycheck:.2f} per week.")

if __name__ == "__main__":
    main()