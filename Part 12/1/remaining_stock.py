# Write your solution here:
def sort_by_remaining_stock(items: list):
    def remaining_stock(item):
        return item[2]
    return sorted(items, key=remaining_stock)