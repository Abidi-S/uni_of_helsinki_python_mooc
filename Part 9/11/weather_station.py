# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations = []

    def __str__(self):
        num_observations = self.number_of_observations()
        return f"{self.__name}, {num_observations} observations"

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if len(self.__observations) > 0:
            return self.__observations[-1]
        return ""

    def number_of_observations(self):
        return len(self.__observations)
