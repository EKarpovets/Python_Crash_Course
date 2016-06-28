def make_car(manufacturer, model_name, **user_info):
    """Build a dictionary containing everything we know about a car."""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = model_name

    for key, value in user_info.items():
        profile[key] = value
    return profile

