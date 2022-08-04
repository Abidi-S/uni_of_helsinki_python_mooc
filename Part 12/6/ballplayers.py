class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(team: list):
    return max(team, key=lambda player: player.goals).name

def most_points(team: list):
    most_points = max(team, key=lambda player: player.goals + player.passes)
    return (most_points.name, most_points.number)

def least_minutes(team):
    return min(team, key=lambda player: player.minutes)