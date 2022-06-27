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
    pass

def deleteRecipe(name):
    pass

def addRecipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        "recipe": name,
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

def printAllNames():
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
        action = input()
        if action == '1':
            recipe = input()
            ingredients = input().split()
            meal = input()
            prep_time = input()
            addRecipe()
        elif action == '2':
            deleteRecipe()
        elif action == '3':
            printRecipe()
        elif action == '4':
            printAllNames()
        elif action == '5':
            closeBook()
        else:
            usage()

if __name__ == "__main__":
    main()