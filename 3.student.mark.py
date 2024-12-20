import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0  # Initialize GPA

    def __str__(self):
        return f"{self.student_id}: {self.name} - GPA: {self.gpa:.1f}"


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits  # Add credits attribute

    def __str__(self):
        return f"{self.course_id}: {self.course_name} - Credits: {self.credits}"


class Marks:
    def __init__(self):
        self.marks = {}

    def input_marks(self, students, courses):
        for course in courses:
            for student in students:
                mark = float(input(f"Enter mark for {student.name} in {course.course_name}: "))
                # Round down to 1 decimal place
                mark = math.floor(mark * 10) / 10
                self.marks[(student.student_id, course.course_id)] = mark

    def show_student_marks(self, student, course):
        mark = self.marks.get((student.student_id, course.course_id), "No mark found")
        print(f"Mark for {student.name} in {course.course_name}: {mark}")

    def calculate_gpa(self, students, courses):
        for student in students:
            total_weighted_marks = 0
            total_credits = 0
            for course in courses:
                mark = self.marks.get((student.student_id, course.course_id), 0)
                total_weighted_marks += mark * course.credits
                total_credits += course.credits
            student.gpa = total_weighted_marks / total_credits if total_credits > 0 else 0


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()

    def input_student_info(self):
        count = int(input("Enter the number of students: "))
        for _ in range(count):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (DoB): ")
            self.students.append(Student(student_id, name, dob))

    def input_course_info(self):
        count = int(input("Enter the number of courses: "))
        for _ in range(count):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))  # Input credits for the course
            self.courses.append(Course(course_id, course_name, credits))

    def list_students(self):
        # Sort students by GPA in descending order
        sorted_students = sorted(self.students, key=lambda s: s.gpa, reverse=True)
        for student in sorted_students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            self.marks.show_student_marks(student, course)
        else:
            print("Invalid student ID or course ID.")

    def main(self, stdscr):
        # Main method to run the student management system
        curses.curs_set(0)  # Hide the cursor
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Management System", curses.A_BOLD)
        stdscr.addstr(1, 0, "Input student information:")
        self.input_student_info()
        stdscr.addstr(2, 0, "Input course information:")
        self.input_course_info()
        self.marks.input_marks(self.students, self.courses)
        self.marks.calculate_gpa(self.students ```python
, self.courses)  # Calculate GPA for each student

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Options: 1. List Students 2. List Courses 3. Show Student Marks 4. Exit")
            stdscr.addstr(1, 0, "Choose an option: ")
            choice = stdscr.getstr(2, 0).decode('utf-8')  # Get user input

            if choice == '1':
                stdscr.addstr(3, 0, "Listing Students:")
                self.list_students()  # List all students
                stdscr.addstr(len(self.students) + 4, 0, "Press any key to continue...")
                stdscr.getch()  # Wait for user input
            elif choice == '2':
                stdscr.addstr(3, 0, "Listing Courses:")
                self.list_courses()   # List all courses
                stdscr.addstr(len(self.courses) + 4, 0, "Press any key to continue...")
                stdscr.getch()  # Wait for user input
            elif choice == '3':
                self.show_student_marks()  # Show marks for a specific student
                stdscr.addstr(4, 0, "Press any key to continue...")
                stdscr.getch()  # Wait for user input
            elif choice == '4':
                break  # Exit the loop and end the program
            else:
                stdscr.addstr(3, 0, "Invalid option. Please try again.")  # Handle invalid input
                stdscr.addstr(4, 0, "Press any key to continue...")
                stdscr.getch()  # Wait for user input


if __name__ == "__main__":
    curses.wrapper(StudentManagementSystem().main)  # Run the main method with curses