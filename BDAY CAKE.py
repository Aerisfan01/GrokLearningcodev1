shopping = ['flour', 'milk', 'eggs', 'sugar', 'butter', 'baking powder']
tick = ' ✅'

print("Shopping List ({} items): {}".format(len(shopping), ", ".join(shopping)))

while True:
    found = input("What ingredient did you find? ")
    
    if found in shopping:
        index = shopping.index(found)
        shopping[index] += tick
        print("{} has been found!".format(found))
    else:
        print("Whoops, that's not on the list!")
        
    print("Remaining items: {}".format(", ".join(shopping)))
    
    if all(tick in item for item in shopping):
        break

print("All ingredients have been found! Time to bake a cake!")
