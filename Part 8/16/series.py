# Write your solution here:
class Series:
    def __init__(self, title, num_seasons, genres):
        self.title = title
        self.num_seasons = num_seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        genres_string = ", ".join(self.genres)
        to_print = ""

        if len(self.ratings) > 0:
            avg_rating = sum(self.ratings)/len(self.ratings)
            to_print += f"{self.title} ({self.num_seasons} seasons)\ngenres: {genres_string}\n{len(self.ratings)} ratings, average {avg_rating:.1f} points"
        else:
            to_print += f"{self.title} ({self.num_seasons} seasons)\ngenres: {genres_string}\nno ratings"

        return to_print

    def rate(self, rating: int):
        if rating >= 0:
            self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list):
    is_valid_series = []
    for series in series_list:
        if sum(series.ratings)/len(series.ratings) >= rating:
            is_valid_series.append(series)
    return is_valid_series

def includes_genre(genre: str, series_list: list):
    series_includes_genre = []
    for series in series_list:
        if genre in series.genres:
            series_includes_genre.append(series)
    return series_includes_genre
