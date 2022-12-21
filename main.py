from Project.func_search import recipe_search
from Project.func_search import save_result
from Project.func_search import add_recipe


def run_again():
    ask_again = input('Do you want to search for another recipe? Yes/No ')
    if ask_again == "Yes":
        run()
    else:
        print('I hope you come back!')


def run():
    ingredient = input('Which ingredient do you want to search for? ')  # Ask the user
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print(recipe['calories'])
        print(recipe['dishType'])
        print(recipe['mealType'])
        print(recipe['cuisineType'])
        print()

    save_result(ingredient)
    add_recipe()
    run_again()


run()
