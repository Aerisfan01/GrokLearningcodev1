recipes = {}

while len(recipes) < 5:
    friend = input("Friend: ")
    recipe = input("Which recipe did they recommend? ")
    
    if recipe in recipes:
        print("Someone else already recommended that.")
    else:
        recipes[recipe] = friend
        print(f"{friend} recommended {recipe}!")
        
print("Cookbook complete! Recipes include:")
for recipe, friend in recipes.items():
    print(f"{recipe}: recommended by {friend}")