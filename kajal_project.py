import sys


class Employee:
    company_name = "SEBI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def add_employee(self):
        print(f"Hello {self.name} Your name is {self.employee}")
        print("-" * 70)

    def update_employee(self, updated_employee):
        self.name = updated_employee
        print(f'After updation your profile is : {self.employee}')
        print("-" * 70)

    def salary_increment(self, salary_updation):
        print("Your profile is updated")
        sys.exit()

    @classmethod
    def get_company_name(cls):
        print("=" * 70)
        print(f'Welcome To {cls.company_name}')
        print("=" * 70)

obj = Employee('Jay', 20000)

while True:

    print("""
        A- add employee
        U- Updated employee
        S- salary increment
        E- Exit
    """)
    print("-" * 70)

    choice = input("Enter your choice: ")

    if choice.lower() == "a":

        obj.add_employee()

    elif choice.lower() == "u":
        updated_employee=eval(input("Enter The updated employee: "))
        obj.updated_employee()

    elif choice.lower() == "s":
        salary_updation = eval(input("Enter salary"))
        obj.salary_increment()

    elif choice.lower() == "e":
        sys.exit()

    else:
        print("Please enter valid choice")



obj = Employee('Jay', 20000)
jay.employee_data()
