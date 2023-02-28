color = input("Which colour did you find? ")
num_tins = int(input("Number of tins: "))

if "blue" in color.lower():
    if num_tins >= 10:
        print(f"Amazing! We have more than enough blue paint!")
    else:
        print(f"Excellent! We'll soon have enough paint for the sky!")
elif num_tins < 4:
    print(f"We're running out of {color.lower()} paint. Let's restock!")
else:
    print(f"Great! We have {num_tins} tins of {color.lower()} paint.")
