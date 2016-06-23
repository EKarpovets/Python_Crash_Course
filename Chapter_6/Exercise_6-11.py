cities = {
    'verona': {
        'country': 'italy',
        'population': 260135,
        'fact': 'Juliet lived here',
    },
    'moscow': {
        'country': 'russia',
        'population': 12330155,
        'fact': 'Kusik lives here',
    },
    'london': {
        'country': 'england',
        'population': 8538689,
        'fact': 'The capital of Great Britain',
    }
}
for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print("Country: " + country.title())
    print("Population: " + str(population))
    print("An interesting fact: " + fact)