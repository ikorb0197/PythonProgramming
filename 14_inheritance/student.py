class Student:
    def __init__(self, name, student_id, major):
        self.__name = name
        self.__student_id = student_id
        self.__major = major

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__student_id}, Major: {self.__major}"
    
    def getName(self):
        return self.__name

class UndergraduateStudent(Student):
    # Overriding of methods
    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major)
        self.__year = year

    def __str__(self):
        return super().__str__() + f", Year: {self.__year}"
    
    def getName(self):
        return super().getName()

if __name__ == "__main__":
    student = Student("Jack", "U1010", "Computer Science")
    print(student)

    undergrad = UndergraduateStudent("Alice", "R4564", "Physics", "Freshman")
    print(undergrad)
    print(undergrad.getName())