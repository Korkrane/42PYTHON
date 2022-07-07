from attr import has
from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        for rType in self.recipes_list:
            for i in self.recipes_list[rType]:
                if i.name == name:
                    print(i)
                    print(i.__repr__())
                    return(i)
        print("Recipe unknown")
        return []

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if  recipe_type in self.recipes_list:
            ret = self.recipes_list.get(recipe_type)
            return ret
        else:
            print("Recipe type unknown")
            return []

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            assert recipe and type(recipe) == Recipe, "Fail to add recipe"
            assert hasattr(recipe, 'name') and hasattr(recipe, 'cookLvl') and hasattr(recipe, 'cookTime') and hasattr(recipe, 'ingredients') and hasattr(recipe, 'rType'), "Fail to add recipe"
            self.recipes_list[recipe.rType].append(recipe)
        except AssertionError as e:
            print("AssertionError:", e)
        self.last_update = datetime.now()
