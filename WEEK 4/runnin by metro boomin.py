exercises = {}

while True:
    name = input("Name: ")
    if name == "":
        break
    minutes = int(input("Minutes: "))
    if name in exercises:
        exercises[name] += minutes
    else:
        exercises[name] = minutes

print("Exercise total:")
for name, minutes in exercises.items():
    message = "keep moving, you can do it!"
    if minutes >= 100:
        message = "amazing, you will smash that beep test!"
    print(f"{name}: {minutes} {message}")
