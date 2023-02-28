def calculate_iron(ore):
  # Calculate the Iron from Ore, to 1 decimal place
    iron = ore * 5 / 13
    return round(iron, 1)

ore = int(input("Ore: "))

iron = calculate_iron(ore)

if iron < 5:
    item = "Useless lump"
elif iron < 20:
    item = "Pickaxe"
elif iron < 35:
    item = "Sword"
elif iron < 45:
    item = "Fancy shield"
else:
    item = "Magic amulet"

print(f"{iron} Iron - {item}")
