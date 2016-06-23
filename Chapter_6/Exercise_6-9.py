favorite_places = {
    'andrey': ['magadan', 'moscow', 'st. petersburg'],
    'katya': ['san remo', 'london'],
    'medvedenka': ['postelka'],
    }
for person, places in favorite_places.items():
    if len(places) > 1:
        print(person.title() + "'s favorite places are:")
    else:
        print(person.title() + "'s favorite place is:")
    for place in places:
            print("\t" + place.title())