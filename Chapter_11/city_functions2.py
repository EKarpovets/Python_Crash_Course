def get_formatted_city(city, country, population = ''):
    if population:
        city_and_country = city.title() + ", " + country.title() + ' - population ' + population
    else:
        city_and_country = city.title() + ", " + country.title()
    return city_and_country

