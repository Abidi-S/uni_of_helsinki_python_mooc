# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    contestants = [person1, person2, person3]
    results = []
    for contestant in contestants:
        result = 0
        for key, value in contestant.items():
            if key != "name":
                result += value
        results.append(result)
    return (contestants[results.index(min(results))])

# code i wish i did not write smh smh