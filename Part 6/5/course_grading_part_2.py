# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercises_info = input("Exercises completed: ")
    exam_info = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercises_info = "exercises1.csv"
    exam_info = "exam_points1.csv"

def read_file(file):
    parts_listicle = []
    with open(file) as current_file:
        for line in current_file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            parts_listicle.append(parts)
    return parts_listicle

def process_student_file():
    students = {}
    parts = read_file(student_info)
    for part in parts:
        students[part[0]] = part[1] + " " + part[2].strip()
    return students

def process_exercises_file():
    exercises_data = {}
    parts = read_file(exercises_info)
    for part in parts:
        exercises_data[part[0]] = []
        for exercise in part[1:]:
            exercises_data[part[0]].append(int(exercise))
    return exercises_data

def process_exam_file():
    exam_data = {}
    parts = read_file(exam_info)
    for part in parts:
        exam_data[part[0]] = []
        for exam in part[1:]:
            exam_data[part[0]].append(int(exam))
    return exam_data

def total_exercise_mark():
    exercises_data = process_exercises_file()
    for id, exercises in exercises_data.items():
        exercises_data[id] = sum(exercises)
    return exercises_data

def total_exam_mark():
    exam_data = process_exam_file()
    for id, score in exam_data.items():
        exam_data[id] = sum(score)
    return exam_data

def final_student_mark():
    exercise_mark = total_exercise_mark()
    exam_mark = total_exam_mark()
    final_mark = {}
    for id, mark in exercise_mark.items():
        final_mark[id] = mark//4 + exam_mark[id]
    return final_mark

def grade_classification():
    final_mark = final_student_mark()
    for id, marks in final_mark.items():
        if 0 <= marks <= 14:
            final_mark[id] = 0
        if 15 <= marks <= 17:
            final_mark[id] = 1
        if 18 <= marks <= 20:
            final_mark[id] = 2
        if 21 <= marks <= 23:
            final_mark[id] = 3
        if 24 <= marks <= 27:
            final_mark[id] = 4
        if marks >= 28:
            final_mark[id] = 5
    return final_mark

students = process_student_file()
grades = grade_classification()
for id, name in students.items():
    print(name, grades[id])