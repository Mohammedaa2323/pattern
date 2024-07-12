class Student :
    name:str
    roll_number:int
    course:str
    date_of_birth:str

    def set_stud(this,name,rn,course,dob):
        this.name=name
        this.roll_number=rn
        this.course=course
        this.date_of_birth=dob
    def display_stud(this):
        print(this.name,this.roll_number,this.course,this.date_of_birth)

stud1=Student()
stud1.set_stud("moahmmed",23,"python","10-2-2002")
stud1.display_stud()
stud2=Student()
stud2.set_stud("arya",22,"cma","10-2-2002")
stud2.display_stud()