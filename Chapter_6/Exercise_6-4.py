glossary = {
    'python': 'a programming language',
    'Medvedenka': "Kusik's first bear",
    'Belyash': "the smallest bear who cannot talk",
    'Mishutka': 'the most hairy bear',
    'Andrey': "Kusik's love"
    }

for key in glossary:
    print(key + ": " + glossary[key] + '\n')

glossary['Hohotunchik'] = 'a hooligan who always laughs'

for key in glossary:
    print(key + ": " + glossary[key] + '\n')