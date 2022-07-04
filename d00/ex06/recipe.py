cookbook = {
    'sandwich': {
        'recipe': 'sandwich',
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'recipe': 'cake',
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'recipe': 'salad',
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def closeBook():
    print("\nCookbook close.")
    exit()


def printRecipe(name):
    print()
    try:
        if cookbook[name]:
            print("Recipe for " + name + ":")
            print("Ingredients list:", cookbook[name]['ingredients'])
            print("To be eaten for", cookbook[name]['meal'])
            print("Takes", cookbook[name]['prep_time'], "minutes of cooking")
            print()
    except KeyError:
        print("Recipe unknown\n")
        return


def deleteRecipe(name):
    try:
        del cookbook[name]
        print("\nRecipe removed from cookbook\n")
    except KeyError:
        print("\nRecipe unknown\n")
        return


def addRecipe(name, ingredients, meal, prep_time):
    print(meal)
    try:
        if type(int(prep_time)) == int and name and meal and ingredients:
            cookbook[name] = {
                "recipe": name,
                "ingredients": ingredients,
                "meal": meal,
                "prep_time": prep_time
            }
        else:
            print("Error in your inputs, recipe not added to cookbook")
    except ValueError:
        print("Error in your inputs, recipe not added to cookbook")
    print()


def printAllNames():
    print()
    for recipe in cookbook.keys():
        print(recipe)
    print()


def info():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def usage():
    print("\nThis option does not exist, please type the corresponding number.")
    print("To exit, enter 5\n")


def main():
    while True:
        info()
        action = input(">>")
        if action == '1':
            print("\nRecipe's name:")
            recipe = input(">>")
            print("\nIngredients required (split with a space):")
            ingredients = input(">>").split()
            print("\nMeal:")
            meal = input(">>")
            print("\nPreparation time:")
            prep_time = input(">>")
            addRecipe(recipe, ingredients, meal, prep_time)
        elif action == '2':
            print("\nPlease enter the recipe's name to delete:")
            recipe = input(">>")
            deleteRecipe(recipe)
        elif action == '3':
            print("\nPlease enter the recipe's name to get its details:")
            recipe = input(">>")
            printRecipe(recipe)
        elif action == '4':
            printAllNames()
        elif action == '5':
            closeBook()
        else:
            usage()


if __name__ == "__main__":
    main()
