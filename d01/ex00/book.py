from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            'starter': {},
            'lunch': {},
            'dessert': {}
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        for rType in self.recipes_list.values():
            for rName, recipe in rType.items():
                if rName == name:
                    print(recipe)
                    return recipe
        print("Unknown recipe")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        try:
            for recipe in self.recipes_list[recipe_type]:
                print(recipe)
        except KeyError:
            print("Unknown type of recipe")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            assert recipe and type(recipe) == Recipe, "Fail to add recipe"
            self.recipes_list[recipe.rType][recipe.name] = recipe
        except AssertionError as e:
            print("AssertionError:", e)
        self.last_update = datetime.now()
