# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def set_grade(self, grade):
        self.__grade = grade

class CourseData:
    def __init__(self):
        self.courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.courses:
            self.courses[name] = Course(name, grade, credits)
        if (name in self.courses) and (grade > self.courses[name].grade()):
            self.courses[name].set_grade(grade)

    def get_course(self, name: str):
        if not name in self.courses:
            return None
        return self.courses[name]

    def all_courses(self):
        return self.courses

class CourseDataApplicaton:
    def __init__(self):
        self.course_data = CourseData()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        self.course_data.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        if self.course_data.get_course(name) == None:
            print("no entry for this course")
            return
        print(self.course_data.get_course(name))

    def get_statistics(self):
        total_credits = 0
        completed_courses = 0
        grades = []
        for name, course in self.course_data.all_courses().items():
            completed_courses += 1
            grades.append(int(course.grade()))
            total_credits += int(course.credits())
        print(f"{completed_courses} completed courses, a total of {total_credits} credits")

        mean = 0
        if completed_courses > 0:
            mean = sum(grades)/completed_courses
        print(f"mean {mean:.1f}")

        print("grade distribution")

        i = 5
        while i > 0:
            exes = ""
            for grade in grades:
                exes = grades.count(grade)*"x"
            print(f"{i}: {exes}")
            i -= 1

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()

application = CourseDataApplicaton()
application.execute()
