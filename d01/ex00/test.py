from book import Book
from recipe import Recipe

myBook = Book("cookbook")
recipe1 = Recipe("sandwich", 1, 10, ['ham', 'bread', 'cheese', 'tomatoes'], '', 'lunch')
recipeFail = Recipe("sandwich", 1, 10, ['ham', 'bread', 'cheese', 'tomatoes'], '', 'test')
recipe2 = Recipe("cake", 5, 60, ['flour', 'sugar', 'eggs'], 'Better hot', 'dessert')
recipe3 = Recipe("salad", 3, 15, ['avocado', 'arugula', 'tomatoes', 'spinach'], 'Better cold', 'starter')
recipe4 = Recipe("chips", 1, 20, ['potatoes', 'salt',], 'use oven', 'lunch')

to_print1 = str(recipe1)
print(to_print1)
print()

myBook.get_recipes_by_types('lunch')
myBook.add_recipe(recipe1)
myBook.add_recipe(recipe4)
myBook.add_recipe("lol")
myBook.get_recipes_by_types('lunch')
myBook.get_recipes_by_types('tost')
myBook.get_recipe_by_name('sandwich')
