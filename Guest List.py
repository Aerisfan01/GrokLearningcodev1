guests = ['Jane', 'Johnno', 'Dazza', 'Beryl', 'Kylie', 'Noa', 'Ainjewel', 'Brie', 'Wengie']

# Add your code after this.
guest_name = input('Guest name: ')

if guest_name in guests:
    print(f"{guest_name} is on the list!")
else:
    print(f"{guest_name} is not invited.")