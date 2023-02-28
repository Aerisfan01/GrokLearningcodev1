print("Let's start the walk-a-thon!")
participants = {}  # dictionary to store participant names and their distances walked
total_distance = 0  # variable to keep track of the total distance walked

while True:
    name = input("Who has recorded a walk? ")
    if name == "":
        break  # exit the loop if no name is entered

    distance = float(input("How far did they walk? "))
    total_distance += distance  # update the total distance walked

    if name in participants:
        participants[name] += distance  # add distance walked to existing participant
        print(f"Another walk from {name}. Well done on another {participants[name]:.1f} km!")
    else:
        participants[name] = distance  # add new participant
        print(f"That's a first time for {name}! They walked {distance:.1f} km!")

print(f"Thanks for taking part in the walk-a-thon! We walked a total of {total_distance:.2f} km!")
print("Here is a list of merit certificate winners:")
for name in sorted(participants):
    print("🏅", name)
