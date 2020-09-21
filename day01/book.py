from recipe import Recipe
import datetime


class Book(object):
    def __init__(
        self,
        name: str,
        # creation_date: datetime,
        # last_update: datetime,
        # recipes_list={"starter": [], "lunch": [], "dessert": []},
    ):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        print(f"The {recipe_type}s are:")
        for recipe in self.recipes_list[recipe_type]:
            print(recipe.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("The recipe must be of type Recipe")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            last_update = datetime.datetime.now()
        print(
            "The book was updated on "
            + last_update.strftime("%d/%m/%y" + " at " + "%H:%M ")
        )


if __name__ == "__main__":
    recipe = Recipe("Tarte", 4, 60, ["pommes", "poires"], "Salut", "starter")
    recipe_two = Recipe("Pie", 4, 60, ["apples", "pears"], "Hello", "dessert")
    recipe_three = Recipe("Tourte", 4, 60, ["apples", "pears"], "Hello", "dessert")
    book = Book("Recettes")
    book.add_recipe(recipe)
    book.add_recipe(recipe_two)
    book.add_recipe(recipe_three)
    book.get_recipe_by_name("Tarte")
    book.get_recipes_by_types("dessert")
