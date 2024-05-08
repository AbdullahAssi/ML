class Person:
    def __init__(self, Age, Name, Address):
        self.Age = Age
        self.Name = Name
        self.address = Address
        
    def display_info(self):
        print(f"Name: {self.Name}\nAge: {self.Age}\nAddress: {self.address}")


class Employee(Person):
    def __init__(self, Age, Name, Address, Employee_id, Department, Salary):
        super().__init__(Age, Name, Address)
        self.Employee_id = Employee_id
        self.Department = Department
        self.Salary = int(Salary)  
        
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.Employee_id}\nDepartment: {self.Department}\nSalary: {self.Salary}")

    def calculate_salary(self):
        print(f"Monthly Salary: {self.Salary/12}")


class Faculty(Employee):
    def __init__(self, Age, Name, Address, Employee_id, Department, Salary, teaching_subject):
        super().__init__(Age, Name, Address, Employee_id, Department, Salary)
        self.teaching_subject = teaching_subject
        
    def teach_course(self):
        print(f"Teaching Subject: {self.teaching_subject}")


class Student(Person):
    def __init__(self, Age, Name, Address, Student_id, major, gpa):
        super().__init__(Age, Name, Address)
        self.Student_id = Student_id
        self.major = major
        self.gpa = gpa
                
    def display_academics(self):
        print(f"Student ID: {self.Student_id}\nStudent Major: {self.major}\nStudent GPA: {self.gpa}")


def print_person_info(person):
    if isinstance(person, Student):
        person.display_info()
        person.display_academics()
    elif isinstance(person, Employee):
        person.display_info()
        person.calculate_salary()
    elif isinstance(person, Faculty):
        person.display_info()
        person.teach_course()
    else:
        person.display_info()



# me = Person("21","Abdullah", "Islamabad")
# me.Display_info()
emp = Employee("21","Abdullah", "Islamabad","1234","IT", 100000)
# emp.Display_info()
# emp.calculate_salary()

fac1 = Faculty("21","Abdullah", "Islamabad","1234","IT","100000","Python")
# fac.teach_course()

student = Student("21", "Abdullah", "Islamabad", "1234", "IT", "3.5")

person_list = [emp, fac1, student]

for person in person_list:
    print_person_info(person)
