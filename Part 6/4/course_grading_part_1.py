# write your solution here
# if False:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
# else:
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

students = {}
with open(student_info) as student_file:
    for line in student_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2].strip()

exercises = {}
with open(exercise_data) as exercise_file:
    for line in exercise_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for exercise in parts[1:]:
            exercises[parts[0]].append(int(exercise))

for id, names in students.items():
    if id in exercises:
        grade = sum(exercises[id])
        print(f"{students[id]} {grade}")
