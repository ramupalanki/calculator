class Course:
    def __init__(self, course_id, name, mentor):
        self.course_id = course_id
        self.name = name
        self.mentor = mentor

    def display_course(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.name}")
        print(f"Mentor: {self.mentor}")


course = Course(
    "PY101",
    "Python Programming",
    
    "Ramu"
)

course.display_course()
