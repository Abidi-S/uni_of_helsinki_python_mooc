# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([word for word in string if word not in forbidden])
