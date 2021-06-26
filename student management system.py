import sys
print("*"*60)
print("********Welcome to student Management system ******")
db={'jay':{'name':'jay','marks':77,'roll_no':11}}
#to store all student at one place we can use database and that is db
print("*"*60)
print(''''
1:List of students
2:Add student
3:update student Information
4:Delete student''')

print("*"*60)

def dashboard():
    print("*"*60)
    print(''''
    1.List of students
    2.AAdd student
    3:Update student
    4.Delete student''')

print("*"*60)

def add_student():
    print(f"*******Add Student Here*******")

    name={}  #to store each student information

    s_name = input("Enter student name:")
    s_marks = eval(input("Enter studnet marks"))
    s_rollno = eval(input("Enter student Roll_no"))

    name['name']=s_name
    name['marks']=s.marks
    name['roll_no']= s_roll_no
    db[s_name]=name
    print(f"student {s_name} is added successfully to the database")

def list_of_student():
    print("******List of students******")
    for students in db:
        print(f"student name is:{db[student]['name']}")
        print(f"Student marks are:{db[student]['marks']}")
        print(f"student roll number:{db[student]['roll_no']}")

    print("*"*60)

def update_student():
    print(f"*******Update Student Here*****")
    s_name=input("Enter student name to update")
    db[s_name]['name']=input("Enter student updated name:")
    db[s_name]['marks']=input("Enter student updated marks")
    db[s_name]['roll_no']=input("Enter student updated roll number:")
    print(f'student{s_name} is updated successfully to the database')

def deletestudent():
    printf("******Delete student here*******")
    print(db)
    s_name=input("Enter student name to delete")
    del db[s_name]
    print(f'student{s_name} is deleted successfully from database')

while True:
    choice = input("Enter your choice:")
    print()
    if choice=='1':
        list_of_students()

    elif choice=='2':
        add_student()

    elif choice=='3':
        update_student()

    elif choice=='4':
        deletestudent()

    else:
        print("Enter valid choice")

    ch=input("do you want to continue program?[yes/No")

    if ch=='Yes':
        dashboard()
    else:
        break

