class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    return list(filter(lambda attempt: attempt.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return(list(filter(lambda attempt: attempt.grade == grade, attempts)))

def passed_students(attempts: list, course: str):
    students = filter(lambda attempt: attempt.grade > 0 and attempt.course_name == course, attempts)
    return sorted(list(map(lambda student: student.student_name, students)))

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
# s4 = CourseAttempt("Niles Nerd", "Networking", 3)
# passed_students([s1, s2, s3, s4], "Introduction to Programming")