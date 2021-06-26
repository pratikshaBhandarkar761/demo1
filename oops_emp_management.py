class Employee:
    def __init__(self,id,salary):
        self.empdetails   = {}
        

    def display(self):
        print(f'Employee  having id {self.id} and salary is {self.salary}')

    def addemp(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
        self.empdetails.update({"name":self.name,"id":self.id,"salary":self.salary})
        print("Employee added successfully")

    def update(self,name,salry):
        self.name = input("Enter Employee name")

        parameter = eval(input("""Enter which parameter you want to update:

                          1:name
                          2:salary
                          3:Both"""))

        if parameter == 1:
            self.name = eval(input("Enter Updated name"))
            self.empdetails.update({"name": self.name})

        if parameter == 2:
            self.salary = input("Enter Updated salary")
            self.empdetails.update({"name": self.name, "id": self.id, "salary": self.salary})
            print("Salary updated successfully")

        if parameter == 3:
            self.name = eval(input("Enter Updated name"))
            self.salary = input("Enter Updated salary")
            self.empdetails.update({"name": self.name, "id": self.id, "salary": self.salary})
            print("Salary and Department updated successfully")


    def remove(self,id):
        self.emplist.pop(self.name)

c =  Employee(5,456)
c.update("seeta")

