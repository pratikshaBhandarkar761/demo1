
print("+" * 70)
print("""
    Welcome To Employee Management System

            Menu
        1:Add Employee Data
        2:Update Employee
        3:Remove Employee Data
        4:Show All Data""")
print("+" * 70)
Database = {'Name': 'Atul', 'ID': 101, 'Department': 'IT', 'Salary': 20000}  # Empty dictionary to store all data


def add_emp_data():
    # key in database
    name = {}

    # taking input for values syntax to add data in dict= dict[key]=value
    emp_name = input("Enter Employee Name")
    emp_id = eval(input("Enter Employee Id"))
    emp_sal = eval(input("Enter salary"))
    emp_dept = input("Enter Employee Department")

    # assigning input values to keys for name

    name['Name'] = emp_name
    name['id'] = emp_id
    name['sal'] = emp_sal
    name['department'] = emp_dept

    Database[emp_name] = name  # this is a key value for database

    print(f"Employee {emp_name}'s data added successfully")


def update():
    emp_name = input("Enter Employee name")

    parameter = eval(input("""Enter which parameter you want to update:

                      1:Salary
                      2:Department
                      3:Both"""))

    if parameter == 1:
        emp_sal = eval(input("Enter Updated Salary"))
        Database[emp_name]['sal'] = emp_sal
        print("Salary updated successfully")

    if parameter == 2:
        emp_dept = input("Enter Updated Department")
        Database[emp_name]['department'] = emp_dept
        print("Salary updated successfully")

    if parameter == 3:
        emp_sal = eval(input("Enter Updated Salary"))
        Database[emp_name]['sal'] = emp_sal

        emp_dept = input("Enter Updated Department")
        Database[emp_name]['department'] = emp_dept
        print("Salary and Department updated successfully")


def remove():
    emp_name = input("Enter Employee name")
    del Database[emp_name]
    print(f"Data of {emp_name} removed successfully")



def display1():
    for name in Database:
        print(f" {Database[name]}",end="")



while True:

    choice = eval(input('Enter your choice: '))
    if choice == 1:
        add_emp_data()
    elif choice == 2:
        update()
    elif choice == 3:
        remove()
    elif choice == 4:
        display1()
    else:
        print("Pls Enter Valid Choice")

    ch = input("Do you want to continue y/n: ")
    ch = ch.lower()
    if ch != "y":
        break
