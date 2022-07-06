import time

availableType = ['starter', 'lunch', 'dessert']


class Recipe:
    def __init__(self, name, cookLvl, cookTime, ingredients, description, rType):
        try:
            assert name and type(name) == str, "recipe name"
            assert cookLvl and type(cookLvl) == int and cookLvl > 0 and cookLvl <= 5, "recipe cookLvl"
            assert cookTime and type(cookTime) == int and cookTime > 0, "recipe cookTime"
            assert ingredients and type(ingredients) == list and all(type(i) == str for i in ingredients), "recipe ingredients"
            assert description is None or type(description) == str, "recipe name"
            assert rType and type(rType) == str and rType in availableType, "recipe rType"
            self.name = name
            self.cookLvl = cookLvl
            self.cookTime = cookTime
            self.ingredients = ingredients
            self.description = description
            self.rType = rType
        except AssertionError as e:
            print("AssertionError:", e)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        data = []
        data.append("===== " + self.name + " recipe ====")
        data.append("cookLvl      -> " + str(self.cookLvl))
        data.append("cookTime     -> " + str(self.cookTime))
        data.append("ingredients  -> " + str(self.ingredients))
        if self.description:
            data.append("description  -> " + self.description)
        else:
            data.append("description  -> No description provided")
        data.append("rType        -> " + self.rType)
        txt = "\n".join((map(str, data)))
        return txt
