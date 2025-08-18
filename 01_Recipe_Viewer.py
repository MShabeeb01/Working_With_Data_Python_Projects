# Step-1: Load recipe from file
def load_recipes(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('Ingredients: ', '').strip()
                    instructions = lines[2].replace('Instructions:', '').strip()
                    recipe_dict[name] = {
                        "ingredients": ingredients,
                        "instructions": instructions
                    }
            return recipe_dict
    except FileNotFoundError:
        print("File not found")
        return {}

# Step-2: Display recipe menu
def show_menu():
    print("\n--- Recipe Viewer Menu ---")
    print("1. View recipe by name")
    print("2. List all recipes")
    print("3. Exit")

# Step-3: Display recipe details
def view_recipe(recipes):
    name = input("Enter the name of the recipe: ").strip().lower()

    # Build a lowercase lookup dictionary
    recipes_lower = {k.lower(): (k, v) for k, v in recipes.items()}

    if name in recipes_lower:
        original_name, recipe = recipes_lower[name]
        print(f"\n--- Recipe {original_name} Details ---")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Instructions: {recipe['instructions']}")
    else:
        print("Recipe not found.")

# Step-4: Main program
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        view_recipe(recipes)
    elif choice == '2':
        print("\n--- All Recipes ---")
        for name in recipes:
            print(name)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")




# 📌 Function Explanations

# 1. load_recipes(file_path)
#    - Opens the given recipe file (recipes.txt).
#    - Reads its entire content.
#    - Splits recipes by double newlines ("\n\n").
#    - For each recipe:
#        * Extracts the name (first line).
#        * Extracts ingredients (second line, after "Ingredients:").
#        * Extracts instructions (third line, after "Instructions:").
#    - Stores recipes in a dictionary in the format:
#        { "RecipeName": {"ingredients": "...", "instructions": "..."} }
#    - Returns this dictionary.
#    - Handles missing file error safely (prints "File not found").

# 2. show_menu()
#    - Prints the main menu options for the user.
#    - Options:
#        1. View recipe by name
#        2. List all available recipes
#        3. Exit the program

# 3. view_recipe(recipes)
#    - Asks user for a recipe name (case-insensitive).
#    - Looks up the recipe in the dictionary.
#    - If found:
#        * Displays the recipe name
#        * Displays ingredients
#        * Displays instructions
#    - If not found, prints "Recipe not found."

# 4. Main program loop
#    - Loads recipes from "recipes.txt" using load_recipes().
#    - Runs an infinite loop until the user chooses to exit.
#    - In each loop:
#        * Calls show_menu() to display options.
#        * Accepts user choice.
#        * If choice is:
#            '1' → Calls view_recipe() to show details of one recipe.
#            '2' → Lists all available recipes.
#            '3' → Exits the program (breaks loop).
#            Else → Prints "Invalid choice".
