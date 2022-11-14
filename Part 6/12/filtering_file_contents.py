# Write your solution here
def process_file(filename):
    sums = []
    addition_sums = []
    subtraction_sums = []
    with open(filename) as solutions:
        for line in solutions:
            parts = line.strip().split(";")
            sums.append(parts)
            if "+" in parts[1]:
                addition_sums.append([parts[0], parts[1].split("+"), parts[2]])
            else:
                subtraction_sums.append([parts[0], parts[1].split("-"), parts[2]])

    return (sums, addition_sums, subtraction_sums)

def filter_solutions():
    sums, addition_sums, subtraction_sums = process_file("solutions.csv")
    correct = []
    incorrect = []

    for [name, values, result] in addition_sums:
        if int(result) == sum(int(x) for x in values):
            correct.append([name, values, result])
        else:
            incorrect.append([name, values, result])

    for [name, values, result] in subtraction_sums:
        difference = int(values[0]) - int(values[1])
        # print(difference)
        if difference == int(result):
            correct.append([name, values, result])
        else:
            incorrect.append([name, values, result])

    with open("correct.csv", 'w') as correct_file:
        for item in sums:
            for [name, values, result] in correct:
                if item[0] == name and item[2] == result:
                    csv_string = f"{item[0]};{item[1]};{item[2]}"
                    correct_file.write(csv_string+"\n")

    with open("incorrect.csv", "w") as incorrect_file:
        for item in sums:
            for [name, values, result] in incorrect:
                if item[0] == name and item[2] == result:
                    csv_string = f"{item[0]};{item[1]};{item[2]}"
                    incorrect_file.write(csv_string+"\n")
