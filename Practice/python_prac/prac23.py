class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credits: {self.credits}")

class TheoryCourse(Course):
    def __init__(self, course_code, course_name, credits, lecture_hours):
        super().__init__(course_code, course_name, credits)
        self.lecture_hours = lecture_hours

    def display_lecture_hours(self):
        print(f"Lecture Hours: {self.lecture_hours}")

class LabCourse(Course):
    def __init__(self, course_code, course_name, credits, lab_hours, prerequisites):
        super().__init__(course_code, course_name, credits)
        self.lab_hours = lab_hours
        self.prerequisites = prerequisites

    def display_lab_hours(self):
        print(f"Lab Hours: {self.lab_hours}")

    def check_prerequisites(self, completed_courses):
        missing_prerequisites = [course for course in self.prerequisites if course not in completed_courses]
        if not missing_prerequisites:
            print("All prerequisites are completed.")
        else:
            print("Missing prerequisites:", missing_prerequisites)

class ProjectCourse(TheoryCourse):
    def __init__(self, course_code, course_name, credits, lecture_hours, project_duration):
        super().__init__(course_code, course_name, credits, lecture_hours)
        self.project_duration = project_duration

    def display_project_duration(self):
        print(f"Project Duration: {self.project_duration} weeks")

def print_course_info(course):
    course.display_info()
    if isinstance(course, TheoryCourse):
        course.display_lecture_hours()
    if isinstance(course, LabCourse):
        course.display_lab_hours()
    if isinstance(course, ProjectCourse):
        course.display_project_duration()

student_courses = {}

def print_student_courses(student_id):
    courses = student_courses.get(student_id, [])
    for course in courses:
        print_course_info(course)
        print() 


course1 = TheoryCourse("CS101", "Intro to AI", 3, 4)
course2 = LabCourse("CS102", "DATABASE Lab", 1, 2, ["CS101"])
course3 = ProjectCourse("CS201", "Machine Learning  Project", 3, 3, 12)


student_courses["student1"] = [course1, course2, course3]


print_student_courses("student1")
