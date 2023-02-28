options = []

while len(options) < 3:
    username = input('Username: ')
    if 'dais' in username.lower():
        options.append(username)

options.sort(reverse=True)
print('Proposals: ' + ', '.join(options))
