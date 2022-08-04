class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):
    def length(route):
        return route.length
    return sorted(routes, key=length, reverse=True)

def sort_by_difficulty(routes: list):
    def difficulty(route):
        return route.grade
    # don't sort twice, rewrite
    return sorted(sort_by_length(routes), key=difficulty, reverse=True)
