dances = ['ballet', 'tap', 'jazz', 'belly', 'contemporary', 'ballroom', 'salsa', 'step', 'swing', 'irish', 'modern', 'shuffle', 'floss', 'twisting', 'macarena', 'interpretive', 'wobble', 'flick', 'stomp', 'tango']
ultra_viral_count = 0

def viral_check(name):
    #Find how viral this dance will go
    if name in dances:
        level = 'nowhere, the dance already exists!'
    elif len(name) == 8:
        level = 'not viral!'
    elif len(name) < 4:
        level = 'slightly viral!'
    elif 'j' in name:
        level = 'somewhat viral!'
    else:
        level = 'ultra viral!'
    
    if level == 'ultra viral!':
        global ultra_viral_count
        ultra_viral_count += 1
    
    return level

dance_names = input("Enter names: ").split()

for name in dance_names:
    level = viral_check(name)
    if level != 'ultra viral!':
        print("The '{}' will go {}".format(name, level))
        
print("Ultra Viral names: {}".format(ultra_viral_count))
dances = ['ballet', 'tap', 'jazz', 'belly', 'contemporary', 'ballroom', 'salsa', 'step', 'swing', 'irish', 'modern', 'shuffle', 'floss', 'twisting', 'macarena', 'interpretive', 'wobble', 'flick', 'stomp', 'tango']

def viral_check(name):
  #Find how viral this dance will go
  level = ''#Write the rest of your program after this.