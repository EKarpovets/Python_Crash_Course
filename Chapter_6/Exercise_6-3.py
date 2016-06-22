glossary = {
    'python': 'a programming language',
    'Medvedenka': "Kusik's first bear",
    'Belyash': "the smallest bear who cannot talk",
    'Mishutka': 'the most hairy bear',
    'Andrey': "Kusik's love"
    }
print("python: "+ glossary['python'] + '\n')
print("Medvedenka: "+ glossary['Medvedenka'] + '\n')
print("Belyash: "+ glossary['Belyash'] + '\n')
print("Mishutka: "+ glossary['Mishutka'] + '\n')
print("Andrey: "+ glossary['Andrey'] + '\n')

for key in glossary:
    print(key + ": " + glossary[key] + '\n')

print(glossary.items())