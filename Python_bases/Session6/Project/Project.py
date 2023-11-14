# Libraries
from pathlib import Path
from os import system

# Variables
current_key = ''
menu_key = 'm'
exit_key = 'e'
book_opened = True
categories_path = Path(Path.home(), "Recetas")
categories_folders = []
recipes_files = []


# Methods
def option_selected():
    chosen_option = 0
    is_valid = False
    possible_options = [1, 2, 3, 4, 5, 6]

    while not is_valid:
        chosen_option = input("Which option do you want (1,2,3,4,5 or 6)? ")
        if int(chosen_option) in possible_options and len(chosen_option) == 1:
            is_valid = True
        else:
            print("You didn't choose a valid option")
    return int(chosen_option)


def key_pressed():
    chosen_letter = ''
    is_valid = False
    possible_keys = (menu_key, exit_key)

    while not is_valid:
        chosen_letter = input("Do you want to continue ('m') or exit ('e')? ")
        if chosen_letter in possible_keys and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You didn't choose a valid letter")
    return chosen_letter


def select_category():
    chosen_category = ''
    is_valid = False

    while not is_valid:
        chosen_category = input("Select a category:  ")
        if chosen_category in categories_folders:
            is_valid = True
        else:
            print("You didn't choose a valid category")
    return Path(categories_path, chosen_category)


def select_recipe(category):
    chosen_recipe = ''
    recipe = ''
    is_valid = False

    for file in category.iterdir():
        recipes_files.append(file.stem)
    print(recipes_files)

    while not is_valid:
        chosen_recipe = input("Select a recipe: ")
        if chosen_recipe in recipes_files:
            recipe = chosen_recipe + '.txt'
            is_valid = True
        else:
            print("You didn't choose a valid recipe")
    return Path(category, recipe)


def create_recipe(category):
    recipe_name = input("What's the name of the new recipe? ")
    recipe_text = input("What's the recipe about? ")
    recipe_file = open(Path(category, recipe_name + '.txt'), 'w')
    recipe_file.write(recipe_text)
    recipe_file.close()
    print(f"Recipe --> {recipe_name} has been added in category {category.name}.")


# Main loop
while book_opened:
    # Welcome the user to the receipe folder structure and update Recetas categories
    print(f"Welcome chef! This is your recipe book "
          f"and these are the categories that you have in this directory:\n")
    for folder in categories_path.iterdir():
        categories_folders.append(folder.name)
        print(folder)

    # User chooses an option (Option1, Option2, Option3, Option4, Option5, Option6)
    option = option_selected()
    if option == 1:
        print("\nOption 1 was selected:\n")
        category_dir = select_category()
        recipe_dir = select_recipe(category_dir)
        recipe_text = open(recipe_dir, 'r')
        print(recipe_text.read())
        recipe_text.close()

    elif option == 2:
        print("\nOption 2 was selected:\n")
        category_dir = select_category()
        create_recipe(category_dir)

    elif option == 3:
        print("\nOption 3 was selected:\n")
        new_category = input("Which category would you like to create? ")
        new_category_dir = Path(categories_path, new_category)
        new_category_dir.mkdir()
        print(f"\nCategory {new_category} has been added.")

    elif option == 4:
        print("\nOption 4 was selected:\n")
        category_dir = select_category()
        recipe_dir = select_recipe(category_dir)
        recipe_dir.unlink()

    elif option == 5:
        print("\nOption 5 was selected:\n")
        category_dir = select_category()
        category_dir.rmdir()
        print(f"\nCategory {category_dir.name} has been removed.")

    elif option == 6:
        print("\nOption 6 was selected:\nHave a nice day!!")
        break

    # Ask user if he wants to continue or not.
    # In case the user continues, we clear the console
    current_key = key_pressed()
    if current_key == exit_key:
        book_opened = False
    else:
        system('cls')
