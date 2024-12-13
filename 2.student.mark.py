class Student:
    def __init__(self, student_id, name, dob):
        # Initialize a student with ID, name, and date of birth
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        # String representation of the student
        return f"{self.student_id}: {self.name}"


class Course:
    def __init__(self, course_id, course_name):
        # Initialize a course with ID and name
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        # String representation of the course
        return f"{self.course_id}: {self.course_name}"


class Marks:
    def __init__(self):
        # Initialize a dictionary to store marks
        self.marks = {}

    def input_marks(self, students, courses):
        # Input marks for each student in each course
        for course in courses:
            for student in students:
                mark = float(input(f"Enter mark for {student.name} in {course.course_name}: "))
                self.marks[(student.student_id, course.course_id)] = mark

    def show_student_marks(self, student, course):
        # Display the mark for a specific student in a specific course
        mark = self.marks.get((student.student_id, course.course_id), "No mark found")
        print(f"Mark for {student.name} in {course.course_name}: {mark}")


class StudentManagementSystem:
    def __init__(self):
        # Initialize lists to store students and courses, and a Marks object
        self.students = []
        self.courses = []
        self.marks = Marks()

    def input_student_info(self):
        # Input information for multiple students
        count = int(input("Enter the number of students: "))
        for _ in range(count):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (DoB): ")
            self.students.append(Student(student_id, name, dob))

    def input_course_info(self):
        # Input information for multiple courses
        count = int(input("Enter the number of courses: "))
        for _ in range(count):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))

    def list_students(self):
        # List all students
        for student in self.students:
            print(student)

    def list_courses(self):
        # List all courses
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        # Show marks for a specific student in a specific course
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            self.marks.show_student_marks(student, course)
        else:
            print("Invalid student ID or course ID.")

    def main(self):
        # Main method to run the student management system
        self.input_student_info()  # Input student information
        self.input_course_info()    # Input course information
        self.marks.input_marks(self.students, self.courses)  # Input marks for students

        while True:
            # Display options to the user
            print("\nOptions: 1. List Students 2. List Courses 3. Show Student Marks 4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.list_students()  # List all students
            elif choice == '2':
                self.list_courses()   # List all courses
            elif choice == '3':
                self.show_student_marks()  # Show marks for a specific student
            elif choice == '4':
                break  # Exit the loop and end the program
            else:
                print("Invalid option. Please try again.")  # Handle invalid input


if __name__ == "__main__":
    system = StudentManagementSystem()  # Create an instance of the system
    system.main()  # Run the main method