def tall_enough(height):
  # Write your function here.
    if height >= 130:
        return 'ship of the desert'
    elif height >= 100:
        return 'pony'
    else:
        return 'teacups'
 

# Write the rest of your program here.
height = int(input('How tall are you? '))
ride = tall_enough(height)
print(f"You can ride the {ride}!")