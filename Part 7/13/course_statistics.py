# Write your solution here
import urllib.request
import json
import math

def retrieve_all():
    data = urllib.request.urlopen(" https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = data.read()
    courses = json.loads(data)

    tupled_listicle = []
    for course in courses:
        if course["enabled"] == True:
            tupled = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            tupled_listicle.append(tupled)
    return tupled_listicle

def retrieve_course(course_name: str):
    data = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = data.read()
    course_stats = json.loads(data)

    weeks = 0
    students = []
    total_hours = 0
    total_exercises = 0
    for key, value in course_stats.items():
        weeks += 1
        students.append(value["students"])
        total_hours += value["hour_total"]
        total_exercises += value["exercise_total"]

    max_students = max(students)
    hours_average = math.floor(total_hours/max_students)
    exercises_average = math.floor(total_exercises/max_students)
    return {"weeks": weeks, "students": max_students, "hours": total_hours, "hours_average": hours_average, "exercises": total_exercises, "exercises_average": exercises_average}
