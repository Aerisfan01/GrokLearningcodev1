shopping = ['flour', 'milk', 'eggs', 'sugar', 'butter', 'baking powder']
tick = ' ✅'
print("Shopping List ({} items): {}".format(len(shopping), ', '.join(shopping)))

while shopping:
    found_item = input("What ingredient did you find? ")
    if found_item in shopping:
        index = shopping.index(found_item)
        shopping[index] = found_item + tick
        print("{} has been found!".format(found_item))
    else:
        print("Whoops, that's not on the list!")
    print("Remaining items: {}".format(', '.join(shopping)))
