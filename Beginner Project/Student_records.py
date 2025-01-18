class Student:
    def __init__(self,name,roll_no,coarse):
        self.name = name
        self.roll_no = roll_no
        self.coarse = coarse
    def display_info(self):
        return f'Name: {self.name}, Roll No.: {self.roll_no}, Course: {self.coarse}'

class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self,name,roll_no,coarse):
        if roll_no not in self.students:
            self.students[roll_no] = Student(name,roll_no,coarse)
            return "The student has been added."
        return "The student already exists."
    
    def search_student(self,roll_no):
        if roll_no in self.students:
            stud = self.students[roll_no]
            return f'The name of the student with Roll No {stud.roll_no} is {stud.name}.'
        return "The student does not exist."

    def display_students(self):
        if self.students == []:
            return 'The list of students is empty.'
        return [stud.display_info for stud in self.students.values()]
    
if __name__ == "__main__":
    sm = StudentManagement()
    print("...Welcome to the student management system...")

    while True:
        print('''
              To add a student --> 1
              To search a student --> 2
              To display the list of students --> 3
              To exit --> 4
''')
        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                name = input("Enter the name of the student:")
                roll_no = int(input("Enter the Roll No:"))
                coarse = input("Enter the coarse:")
                print(sm.add_student(name,roll_no,coarse))
            case 2:
                roll_no = int(input("Enter the Roll No:"))
                print(sm.search_student(roll_no))
            case 3:
                print(sm.display_students())
            case 4:
                print("Bye")
                break