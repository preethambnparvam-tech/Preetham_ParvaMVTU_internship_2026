class Student:
    # class variable
    university = "VTU"


    # constructor
    def __init__(self, name, usn, branch, college):
        self.name = name
        self.usn = usn


        # protected variables
        self._branch = branch
        self._college = college


        # private variables
        self.__subjects = {}
        self.__total_marks = 0
        self.__percentage = 0
        self.__grade = None


    # Public method
    def add_subject_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.__subjects[subject] = marks
            print(f"{subject} marks ({marks}) added successfully!")
        else:
            print(f"{marks} is an invalid marks.")


    def calculate_result(self):
        if not self.__subjects:
            print("No subjects added! Please add the subject and marks to find the result.")
            return
       
        self.__total_marks = sum(self.__subjects.values())
        self.__percentage = self.__total_marks / len(self.__subjects)
        self.__grade = self.__calculate_grade()


        print("\nResult calculated successfully!\n")


    def __calculate_grade(self):
        if self.__percentage >= 85:
            return "'A' - Distinction"
        elif self.__percentage >= 70:
            return "'B' - First Class"
        elif self.__percentage >= 60:
            return "'C' - Second Class"
        elif self.__percentage >= 50:
            return "'D' - Third Class"
        else:
            return "'F' - Fail"


    def display_result(self):
        if self.__grade is None:
            print("Please calculate the result first")
            return
       
        print("------------Student Result-------------")
        print(f"Name: {self.name}")
        print(f"USN: {self.usn}")
        print(f"Branch: {self._branch}")
        print(f"College: {self._college}")
        print(f"University: {Student.university}")


        print("\nSubjects and Marks:")
        for subject, marks in self.__subjects.items():
            print(f"{subject}: {marks}")


        print(f"\nTotal Marks: {self.__total_marks}")
        print(f"Percentage: {self.__percentage:.2f}%")
        print(f"Grade: {self.__grade}\n")


std1 = Student("Akshay Rao", "1AB18IS001", "Computer Science", "ABC College")
std2 = Student("Ajay Rao", "1AC20CS001", "Electronics", "ACS College")


std1.add_subject_marks("Physics", 75)
std1.add_subject_marks("Chemistry", 80)
std1.add_subject_marks("Maths", 85)
std1.add_subject_marks("Computer Science", 90)


std1.calculate_result()
std1.display_result()


std2.add_subject_marks("Physics", 80)
std2.add_subject_marks("Chemistry", 85)
std2.add_subject_marks("Maths", 80)
std2.add_subject_marks("Computer Science", 88)


std2.calculate_result()
std2.display_result()
