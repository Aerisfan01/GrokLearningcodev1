party_theme = input("Party theme: ")

# Get the supplies list from the user and split it into a list
supplies = input("Supplies needed: ").split()

# Print the party theme and supplies list
print(f"The {party_theme} party is coming up soon!")
print("We will need to get...")

# Loop over the supplies list and print each item with the 🥳 emoji
for supply in supplies:
    print("🥳 " + supply)

# Print a reminder to invite friends
print(f"Remember to invite your {party_theme} buddies!")