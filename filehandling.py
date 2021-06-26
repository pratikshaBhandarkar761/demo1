#fun1 create data
#fun2 read data
class employee:
    def __init__(self,name,salry,dept):

        self.name = input("Enter name")
        self.salary = input("Enter salary")
        self.dept = input("Enter dept")
    def addemp(self):
        fd = open('emp.txt', 'a')
        l = [self.name,"~",self.salary,"~",self.dept,"~","\n"]
        fd.writelines(l)
        print(f"Employee {self.name} added successfully")
        fd.close()
    def show(self):
        fd = open('emp.txt')
        data = fd.read()
        print(data)
    def increment(self,sal):



e = employee("varad",1500,"cs")
e.increment(200)
