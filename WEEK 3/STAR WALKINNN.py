print("Let's start the walk-a-thon!")
participants = []
total_distance = 0

while True:
    name = input("Who has recorded a walk? ")
    if not name:
        break
    distance = float(input("How far did they walk? "))
    total_distance += distance
    found = False
    for participant in participants:
        if participant['name'] == name:
            participant['distance'] += distance
            print(f"Another walk from {name}. Well done on another {distance} km!")
            found = True
            break
    if not found:
        participants.append({'name': name, 'distance': distance})
        print(f"That's a first time for {name}! They walked {distance} km!")
        
print(f"Thanks for taking part in the walk-a-thon! We walked a total of {total_distance} km!")
print("Here is a list of merit certificate winners:")
for participant in sorted(participants, key=lambda x: x['name']):
    print("🏅", participant['name'])
