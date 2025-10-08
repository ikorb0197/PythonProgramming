class Course:
    def __init__(self, course_name: str):
        self.__course_name: str = course_name
        self.__list_of_students: list[str] = []
    def addStudent(self, student: str):
        if student not in self.getStudents():
            self.__list_of_students.append(student)
        else:
            print(f"{student} is already in this course")
    def getCourseName(self) -> str:
        return self.__course_name
    def getStudents(self) -> list[str]:
        return self.__list_of_students
    def getNumberOfStudents(self) -> int:
        return len(self.__list_of_students)
    def dropStudent(self, student: str):
        if student in self.getStudents():
            self.__list_of_students.remove(student)
            print(f"Dropped student: {student}")
        else:
            print(f"{student} is not in this course")
    def __str__(self) -> str:
        return f"Course name: {self.getCourseName()}, Number of students: {self.getNumberOfStudents()}, Students: {self.getStudents()}"

class InPersonCourse(Course):
    def __init__(self, course_name: str, room_number: str, schedule: str, max_seats: int):
        super().__init__(course_name)
        self.__room_number: str = room_number
        self.__schedule: str = schedule
        self.__max_seats: int = max_seats
    def addStudent(self, student: str):
        if self.getNumberOfStudents() < self.__max_seats:
            super().addStudent(student)
        else:
            print("Course is full")
    def __str__(self) -> str:
        return f"Course name: {self.getCourseName()}, Room number: {self.__room_number}, Schedule: {self.__schedule}, Maximum seats: {self.__max_seats}, Number of students: {self.getNumberOfStudents()}, Students: {self.getStudents()}"

python_online = Course("Python (online)")
python_f2f = InPersonCourse("Python (F2F)", "IST-1026", "MWF 11 am - 11:50 am", 40)
python_online.addStudent("John Buh")
print(python_online)
python_f2f.addStudent("Bih Smith")
python_f2f.addStudent("Tuh Vampire")
python_f2f.dropStudent("Tuh Vampire")
python_f2f.addStudent("Tuh Vampire")
python_f2f.dropStudent("Kuh Walrus")
for i in range(3, 42):
    python_f2f.addStudent("Student " + str(i))
print(python_f2f)