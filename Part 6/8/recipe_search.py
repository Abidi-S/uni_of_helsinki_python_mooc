# Write your solution here
# UGLY CODE
def process_file(filename: str):
    recipes = []
    recipe = []
    with open(filename) as new_file:
        for line in new_file:
            if line == "\n":
                recipes.append(recipe)
                recipe = []
                continue
            recipe.append(line.strip())
        recipes.append(recipe)

    return recipes

def search_by_name(filename: str, word: str):
    recipes = process_file(filename)

    found_recipes = []
    for recipe in recipes:
        if word in recipe[0].lower():
            found_recipes.append(recipe[0])

    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = process_file(filename)

    found_recipes = []
    for recipe in recipes:
        if int(recipe[1]) <= prep_time:
            recipe_info = f"{recipe[0]}, preparation time {recipe[1]} min"
            found_recipes.append(recipe_info)

    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = process_file(filename)

    found_recipes = []
    for recipe in recipes:
        if ingredient in recipe:
            recipe_info = f"{recipe[0]}, preparation time {recipe[1]} min"
            found_recipes.append(recipe_info)

    return found_recipes

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)