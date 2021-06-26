print("-" * 100)
print("*" * 10 + "WELCOME TO EMPLOYEE MANAGEMENT SYSTEM" + '*' * 10)
print("-" * 100)

print('''
                       Menu
                1) Add Employee
                2) Remove Employee
                3) Search Employee
                4) Update Employee
                5) Display ALl Employee
    ''')
print("=" * 70)

database = [{'Name': 'hana', 'id': 1, 'sal': 123}]
print("=" * 70)



def add_employee():
    name = {}
    ename = input("enter name")
    eid = eval(input("Enter id"))
    esal = eval(input("Enter salary"))

    name['Name'] = ename
    name['id'] = eid
    name['sal'] = esal
    print(name)
    print(f"{ename} data added successfully")


def update():
    sn = int(input("Enter serial number to be update"))
    para = input("Enter which parameter you want to update Name/id/sal")

    if para == 'Name':
        ch = input("Enter Updated name")
    if para == 'id':
        ch = input("Enter Updated id")
    if para == 'sal':
        ch = input("Enter Updated sal")

    database[sn][para] = ch
    print(f"{sn} data updated successfully {database[sn]['Name']}")
    print(f"{sn} data updated successfully {database[sn]['id']}")
    print(f"{sn} data updated successfully {database[sn]['sal']}")


def remove():
    ename = input("Enter Employee name to remove")
    database.remove(list[ename])
    print("{ename} data deleted successfully")


def search():
    c = int(input("Enter Employee serial number to search: "))
    if c < len(database):
        print(f"Employee Name is    ----> {database[c]['Name']} ")
        print(f"Employee ID No is ----> {database[c]['id']} ")
        print(f"Employee Salary is  ----> {database[c]['sal']} ")
        # print(db[c])
    else:
        print("Employee is not present")


def display():
    def list_display():
        c = 0
        while c < len(database):
            print(f"Employee Serial number is    ----> {c} ")
            print(f"Employee Name is             ----> {database[c]['Name']} ")
            print(f"Employee ID No is            ----> {database[c]['ID_Num']} ")
            print(f"Employee Salary is           ----> {database[c]['Salary']} ")
            print('-' * 70)
            c += 1


while (1):

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        update()
    elif choice == 3:
        search()
    elif choice == 4:
        remove()
    elif choice == 5:
        display()
    else:
        print("Invalid Choice")

    ch = input("Do you want to continue y/n:")
    ch = ch.lower()
    if ch != 'y':
        break



