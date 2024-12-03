def input_student_count():
    count = int(input("Enter the number of students: "))
    return count

def input_student_info(count):
    students = {}
    for _ in range(count):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DoB): ")
        students[student_id] = {'name': name, 'dob': dob}
    return students

def input_course_count():
    count = int(input("Enter the number of courses: "))
    return count

def input_course_info(count):
    courses = {}
    for _ in range(count):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

def input_marks(students, courses):
    marks = {}
    for course_id in courses.keys():
        for student_id in students.keys():
            mark = float(input(f"Enter mark for {students[student_id]['name']} in {courses[course_id]}: "))
            marks[(student_id, course_id)] = mark
    return marks

def list_courses(courses):
    for course_id, course_name in courses.items():
        print(f"{course_id}: {course_name}")

def list_students(students):
    for student_id, info in students.items():
        print(f"{student_id}: {info['name']}")

def show_student_marks(marks, students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    mark = marks.get((student_id, course_id), "No mark found")
    print(f"Mark for {students[student_id]['name']} in {courses[course_id]}: {mark}")

def main():
    student_count = input_student_count()
    students = input_student_info(student_count)
    course_count = input_course_count()
    courses = input_course_info(course_count)
    marks = input_marks(students, courses)

    while True:
        print("\nOptions: 1. List Students 2. List Courses 3. Show Student Marks 4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_students(students)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            show_student_marks(marks, students, courses)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()