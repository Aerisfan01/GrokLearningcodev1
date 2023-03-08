print("Who dares campaign in the Shadow Realm?")

# initialize variables
gold = 81
shadow_tokens = 2
friends = {}

# get friend names and gold won/lost
while True:
    name = input("Name: ")
    if name == "":
        break
    print(f"Starting amount of gold: {gold}")
    print(f"{name}'s here, starting with {shadow_tokens} shadow tokens of gold!")
    amount = input(f"How much gold did {name} win or lose? ")
    friends[name] = int(amount)

print("\nLet's play!")
for friend in friends:
    print(f"{friend} played and {'won' if friends[friend] > 0 else 'lost'} {abs(friends[friend])} gold coins.")

# calculate remaining gold and shadow tokens
gold += sum(friends.values())
shadow_tokens += gold // 50
gold = gold % 50

print("\nEnd of the campaign! Let's see how everyone did!")
print(f"Total gold remaining: {gold}")
print(f"Total shadow tokens: {shadow_tokens}")
for friend in friends:
    print(f"{friend} {'won' if friends[friend] > 0 else 'lost'} {abs(friends[friend])} gold coins and {'can buy' if friends[friend] >= 50 else 'cannot buy'} shadow tokens.")



#not sure it doesnt work    