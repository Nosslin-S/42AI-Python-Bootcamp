import sys


def print_recipe(cookbook, recipe):
    print("{:21}".format("Name of the recipe : ") + recipe)
    print(
        "{:21}".format("Ingredients needed : ")
        + ", ".join(cookbook[recipe]["ingredients"])
    )
    print("{:21}".format("Meal type : ") + cookbook[recipe]["meal"])
    print(
        "{:21}".format("Preparation time : ")
        + str(cookbook[recipe]["prep_time"])
        + " minutes"
    )
    print("")


def del_recipe(cookbook, recipe):
    del cookbook[recipe]


def add_recipe(cookbook, recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }


def print_cookbook(cookbook):
    for k, v in cookbook.items():
        print_recipe(cookbook, k)


cookbook = {}
add_recipe(cookbook, "sandwich", ["ham", "bread", "cheese", "tomatoes"], "lunch", 10)
add_recipe(cookbook, "cake", ["flour", "sugar", "eggs"], "dessert", 60)
add_recipe(
    cookbook, "salad", ["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15
)

if len(sys.argv) < 2:
    print(
        "You can access the following commands :\n-'print cookbook'\n-'print 'recipe name''\n-'add 'recipe name''\n-'del 'recipe''\n"
    )

print_recipe(cookbook, "salad")
print_cookbook(cookbook)

