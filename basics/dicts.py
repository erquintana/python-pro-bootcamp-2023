# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, places):
    """
    Add a new country to the travel_log list.
    
    Args:
    - country (str): the name of the country to be added.
    - visits (int): the number of times visited the country.
    - places (list): a list of cities visited in the country.
    
    Returns:
    - None
    """
    new_dict_in_list = {}
    new_dict_in_list["country"] = country 
    new_dict_in_list["visits"] = visits
    new_dict_in_list["cities"] = places
    travel_log.append(new_dict_in_list)

# Example usage
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)