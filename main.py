class Person:
    __age = 18

    def __init__(self, name: str, last_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2 and name.isalnum():
            self.__name = name
        else:
            raise ValueError("The name must be alphanumeric and have a length of at least 3 characters")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age

    def show_info(self):
        print(f"Name: {self.name}, Last name: {self.last_name}, Age: {self.age}")


class Teacher(Person):
    def __init__(self, name: str, last_name: str, age: int, teaching_subject: str, work_experience: int):
        super().__init__(name, last_name, age)
        self.teaching_subject = teaching_subject
        self.work_experience = work_experience

    def show_info(self):
        super().show_info()
        print(f"Teaches: {self.teaching_subject}, work experience: {self.work_experience} years")


class Student(Person):
    def __init__(self, name: str, last_name: str, age: int, year_of_study: int, subjects: list[str]):
        super().__init__(name, last_name, age)
        self.year_of_study = year_of_study
        self.subjects = subjects

    def show_info(self):
        print(f"Student: year of study: {self.year_of_study}, subjects: {', '.join(self.subjects)}")


class Subject:
    def __init__(self, subject_name: str, description: str, teacher: Teacher):
        self.subject_name = subject_name
        self.description = description
        self.teacher = teacher
        self.enrolled_students = []

    def add_student(self, student: Student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
        else:
            raise ValueError(f"{student.name} {student.last_name} is already enrolled in {self.subject_name}")

    def remove_student(self, student: Student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        else:
            raise ValueError(f"{student.name} {student.last_name} is not enrolled in {self.subject_name}")

    def show_info(self):
        print(f"Subject: {self.subject_name}")
        print(f"Description: {self.description}")
        print(f"Teacher: {self.teacher.name} {self.teacher.last_name}")
        print(f"Enrolled Students:")
        for student in self.enrolled_students:
            print(f"- {student.name} {student.last_name}")


class Faculty:
    def __init__(self, name: str, address: str, department: str):
        self.name = name
        self.address = address
        self.department = department

    def show_info(self):
        print(f"Faculty: {self.name}")
        print(f"Address: {self.address}")
        print(f"Department: {self.department}")


class Academy:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_student(self, student: Student):
        self.students.append(student)

        def show_info(self):
            print(f"Academy: {self.name}")
            print(f"Address: {self.address}")
            print(f"Teachers:")
            for teacher in self.teachers:
                teacher.show_info()
            print(f"Students:")
            for student in self.students:
                student.show_info()


    try:
        teacher = Teacher("John", "Doe", 30, "Mathematics", 10)
        student_1 = Student("Mike", "Brown", 20, 2024, ["Physics", "Chemistry"])
        student_2 = Student("Alice", "Miller", 19, 2024, ["Mathematics", "English"])

        subject = Subject("Data Science", "Introduction to machine learning and data analysis", teacher)

        subject.add_student(student_1)
        subject.add_student(student_2)

        subject.show_info()

        subject.remove_student(student_2)

        subject.show_info()

        teacher.show_info()

    except ValueError as e:
        print(f"Error: {e}")


