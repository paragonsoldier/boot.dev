def check_ingredient_match(recipe, inventory):
    available_ingredients = []
    missing_ingredients = []
    for ingredient in recipe:
        if ingredient in inventory:
            available_ingredients.append(ingredient)
            continue
        missing_ingredients.append(ingredient)
    percentage_of_required_ingredients = len(available_ingredients) / len(recipe) * 100
    return percentage_of_required_ingredients, missing_ingredients
