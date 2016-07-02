from collections import OrderedDict

glossary = OrderedDict()
glossary['python'] = "a programming language"
glossary['Medvedenka'] = "Kusik's first bear"
glossary['Belyash'] = "the smallest bear who cannot talk"
glossary['Mishutka'] = "the most hairy bear"
glossary['Andrey'] = "Kusik's love"

for key in glossary:
    print(key + ": " + glossary[key] + '\n')

glossary['Hohotunchik'] = 'a hooligan who always laughs'

for key in glossary:
    print(key + ": " + glossary[key] + '\n')

for key, value in glossary.items():
    print("Key: " + key + ", value: " + value)