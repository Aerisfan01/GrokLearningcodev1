start_pop = int(input("Initial population: "))
final_pop = int(input("Final population: "))

years = 0
while start_pop < final_pop:
    start_pop *= 1.37
    years += 1

print(f"It would take {years} years for there to be {final_pop} rabbits.")
