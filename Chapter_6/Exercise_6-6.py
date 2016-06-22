favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

friends = ['jen', 'jane', 'kate', 'edward', 'phil']

for name in friends:
    print(name.title())
    if name in favorite_languages.keys():
        print("Thank you for responding, " + name.title() + "!")
    else:
        print("Please take the poll, " + name.title() + ".")

