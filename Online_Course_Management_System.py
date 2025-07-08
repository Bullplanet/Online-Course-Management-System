# Project - Online Course Management System


class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.user_id = user_id
        self.__email = email

    def get_email(self):
        print(f"Your current email: {self.__email}")
        return self.__email
    
    def set_email(self, new_email):
        if new_email != self.__email:
            self.__email = new_email
            print(f"Your new email is {self.__email}")
        else:
            print("Provide an email you already have account")

    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}"




class Student(User):
    def __init__(self, name, student_id, email):
        super().__init__(name, student_id, email)

        self.enrolled_courses = []

    def enroll(self, course: "Course"):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.enroll_student(self)
            print(f"You successfully enrolled in {course.course_name} course")
        else:
            print(f"You already enrolled in {course.course_name} course")


    def drop(self, course: "Course"):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.unenroll_student(self)
            print(f"You have successfully dropped the {course} course.")
        else:
            print("Enter the course that you already enrolled")

    def view_courses(self):
        if self.enrolled_courses:
            print(f"The courses you are currently in: ")
            for c in self.enrolled_courses:
                print(f"- {c.course_name} ({c.course_code})")
        else:
            print("You're not enrolled in any courses yet.")

    def view_profile(self):
        print(f"Profile: ")
        print(f"- {self.name} (ID: {self.user_id})")
        if self.enrolled_courses:
            for course in self.enrolled_courses:
                if course.instructor:
                    print(f"- {course.course_name} (ID: {course.course_code}) (Instructor: {course.instructor.name})")
                else:
                    print(f"- {course.course_name} (ID: {course.course_code}) (Instructor: Not assigned yet)")
        else:
            print("Didn't enroll in any courses yet.")
            
        
    
    def __str__(self):
        enrolled_names = [course.course_name for course in self.enrolled_courses]
        return f"Student: {self.name}, ID: {self.user_id}, Enrolled Courses: {enrolled_names}"


class Instructor(User):
    def __init__(self, name, instructor_id, email):
        super().__init__(name, instructor_id, email)

        self.courses_taught = []

    def assign_course(self, course: "Course"):
        if course in self.courses_taught:
            print(f"You're already teaching {course.course_name} course")
        else:
            self.courses_taught.append(course)
            course.assign_instructor(self)
            print(f"{course.course_name} course assigned to you")

    def remove_course(self, course: "Course"):
        if course not in self.courses_taught:
            print(f"You are not assigned to {course.course_name}. We can remove only if you are assigned.")
        else:
            self.courses_taught.remove(course)
            course.unassign_instructor(self)
            if course.instructor == self:
                course.instructor = None      
            print(f"You have been unassigned from {course.course_name} course")

    def view_courses_taught(self):
        if self.courses_taught:
            print("All the course you are assigned to:")
            for c in self.courses_taught:
                print(f"- {c.course_name} ({c.course_code})")    
        else:
            print("You're not assigned to any courses yet.")

    def view_enrolled_students(self):
        if not self.courses_taught:
            print("You are not assigned to any course")
            return

        for course in self.courses_taught:
            print(f"\nCourse: {course.course_name} ({course.course_code})")

            if course.students_enrolled:
                print("Enrolled Students")
                for student in course.students_enrolled:
                    print(f"- {student.name} (ID: {student.user_id})")

            else:
                print("No students have enrolled in this course")

    def view_profile(self):
        print("Profile: ")
        print(f"- {self.name} (ID: {self.user_id})")
        if self.courses_taught:
            print(f"\nCourses assigned: ")
            for course in self.courses_taught:
                print(f"- {course.course_name} (ID: {course.course_code})")
                if course.students_enrolled:
                    print(" Enrolled Students: ")
                    for student in course.students_enrolled:
                        print(f"- Student Name: {student.name} (ID: {student.user_id})")
                else:
                    print("No students have enrolled in this course")
        else:
            print("Currently you are not teaching any course")





    def __str__(self):
        teaching_list = [course.course_name for course in self.courses_taught]
        return f"Instructor: {self.name}, ID: {self.user_id}, Currently Teaching: {teaching_list}"



class Course:
    def __init__(self, course_name, course_code, description):
        self.course_name = course_name
        self.course_code = course_code
        self.description = description
        self.instructor = None
        self.students_enrolled = []

    def assign_instructor(self, instructor):
        if self.instructor  is not None:
            print(f"{self.instructor} has already assigned to {self.course_name}")
        else:
            self.instructor = instructor
            print(f"{self.instructor} is assigned to {self.course_name}")


    def unassign_instructor(self, instructor):
        if self.instructor:
            print(f"{self.instructor} has been unassigned from the {self.course_name}")
            self.instructor = None
        else:
            print(f"No instructor is currenlty assigned to {self.course_name}")

    def enroll_student(self, student):
        if student not in self.students_enrolled:
            self.students_enrolled.append(student)
            print(f"{student.name} enrolled in {self.course_code}")
        else:
            print(f"{student.name} already enrolled in {self.course_name}")

    def unenroll_student(self, student):
        if student not in self.students_enrolled:
            print(f"{student.name} is not enrolled in {self.course_name}")
        else:
            self.students_enrolled.remove(student)
            print(f"{student.name} has been unenrolled from {self.course_name}")

    def __str__(self):
        return f"{self.course_name} - {self.course_code} - {self.description} "
    



# # Create courses
python_course = Course("Python Basics", "PY101", "Intro to Python")
java_course = Course("Java Essentials", "JA101", "Learn Java fundamentals")

# # Create instructor
instructor_amy = Instructor("Amy Jackson", "I001", "amy@school.com")

# # Assign courses to instructor
# instructor_amy.assign_course(python_course)
# instructor_amy.assign_course(java_course)

# # Create students
student1 = Student("John Doe", "S001", "john@student.com")
student2 = Student("Emma Stone", "S002", "emma@student.com")

# Enroll students in courses
# student1.enroll(python_course)
# student2.enroll(java_course)

# Now test the function
#instructor_amy.view_enrolled_students()

# Testing the view_profile() for both student and instructor
student2.view_profile()
instructor_amy.view_profile()                   
