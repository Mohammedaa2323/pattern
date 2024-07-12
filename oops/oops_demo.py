class Employee:

    id:int
    name:str
    department:str
    salary:int

    def set_emp(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.department=dep
        self.salary=sal

    def display_emp(self):
        print(self.name,self.id,self.department,self.salary)

emp1=Employee()
emp1.set_emp(123,"suhail","office boy",1000)

emp2=Employee()
emp2.set_emp(321,"prashanth","office boy",1001)

emp1.display_emp()
emp2.display_emp()