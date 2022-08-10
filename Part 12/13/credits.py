from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_courses = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda reduced_sum, t: reduced_sum + t.credits, passed_courses, 0)

def average(attempts: list):
    passed_courses = list(filter(lambda t: t.grade >= 1, attempts))
    return reduce(lambda reduced_sum, item: reduced_sum + item.grade, passed_courses, 0)/len(passed_courses)
