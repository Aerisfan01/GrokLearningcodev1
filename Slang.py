slang = ['GTG', 'LOL', 'IMD', 'IDK', 'IDC', 'CTC?', 'BTW', 'TBH', 'LMK', 'NVM']

text_message = input("Text message: ")

words = text_message.split()

slang_count = 0

for word in words:
    if word in slang:
        slang_count += 1

print("Number of slang words used:", slang_count)
