import requests


def recipe_search(ingredient):
    app_id = "  # First register to get an APP ID and key at https://developer.edamam.com/
    app_key = "
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']


def save_result(ingredient):
    new_item = input('Do you want to save the result? Yes/No ')
    if 'Yes':
        with open('result.txt', 'r') as result_file:
            result = result_file.read()

        result = result + str(recipe_search(ingredient)) + '\n'

        with open('result.txt', 'w+') as result_file:
            result_file.write(result)


def add_recipe():
    new_recipe = input('What recipe would you like to save? ')
    with open('recipes.txt', 'r') as recipes_file:
        recipes = recipes_file.read()

    recipes = recipes + new_recipe + '\n'

    with open('recipes.txt', 'w+') as recipes_file:
        recipes_file.write(recipes)
