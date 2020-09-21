import textwrap


class Recipe(object):
    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: list,
        description: str,
        recipe_type: str,
    ):
        if not isinstance(name, str) or name == "":
            raise TypeError("The name must be a string")
        else:
            self.name = name
        if not isinstance(cooking_lvl, int) or cooking_lvl == "":
            raise TypeError("The cooking level must be a integer")
        else:
            assert (
                cooking_lvl <= 5 and cooking_lvl >= 1
            ), "Cooking level must be between 1 and 5"
            self.cooking_lvl = cooking_lvl
        if not isinstance(cooking_time, int) or cooking_time == "":
            raise TypeError("The cooking time must be an integer")
        else:
            self.cooking_time = cooking_time
        if (
            not all(isinstance(ingredient, str) for ingredient in ingredients)
            or ingredients == ""
        ):
            raise TypeError("The ingredients must be a list of strings")
        else:
            self.ingredients = ingredients
        if not isinstance(description, str):
            raise TypeError("The description must be a string")
        else:
            self.description = description
        if not isinstance(recipe_type, str) or recipe_type == "":
            raise TypeError("The recipe type must be a string")
        else:
            assert (
                recipe_type == "starter"
                or recipe_type == "lunch"
                or recipe_type == "dessert"
            ), "The recipe type must either be 'starter', 'lunch' or 'dessert'"
            self.recipe_type = recipe_type

    def __str__(self):
        return textwrap.dedent(
            f"""
            {'The recipe is :':30} {self.name}
            {'The cooking level is :':30} {self.cooking_lvl}
            {'The cooking time is :':30} {self.cooking_time} minutes
            {'The ingredients needed are :':30} {self.ingredients}
            {'Description of the recipe :':30} {self.description}
            {'Type of recipe :':30} {self.recipe_type}"""
        )


if __name__ == "__main__":
    test = Recipe("Tarte", 4, 60, ["pommes", "poires"], "Salut", "starter")
    print(test)
    print(test.recipe_type)
