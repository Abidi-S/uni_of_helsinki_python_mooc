# Write your solution here:
def sort_by_seasons(items: list):
    def num_seasons(item):
        return item["seasons"]
    return sorted(items, key=num_seasons)