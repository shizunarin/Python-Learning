#6.1
person_info = {
    'First_name': 'Yi',
    'Last_name': 'Wang',
    'Age': 28,
    'City': 'Yokohama'
}
print(person_info['First_name'], person_info['Last_name'], person_info['Age'], person_info['City'])

#6.2
favorite_number = {
    'Ryan': 1,
    'Wang': 2,
    'Yi': 3,
    'Jack': 4
}

print(f"Ryan's favorite number is {favorite_number['Ryan']}")
print(f"Wang's favorite number is {favorite_number['Wang']}")
print(f"Yi's favorite number is {favorite_number['Yi']}")
print(f"Jack's favorite number is {favorite_number['Jack']}")

#6.5
river_dict = {
    'yellow river': 'China',
    'nile': 'Egypt',
    'long river': 'China'
}

for river, country in river_dict.items():
    print(f"\nThe {river.title()} runs through {country.title()}")

for river in set(river_dict.keys()):
    print(river.title())

for country in set(river_dict.values()):
    print(country.title())

#6.6
favorite_languages = {
    'jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

name_person = {'jen', 'edward', 'yi', 'wang'}
for name in name_person:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, Thanks for you cooperative!")
    else:
        print(f"Hi {name.title()}, Plase join us to get a investment!")

#6.7
person_info1 = {
    'First_name': 'Yi',
    'Last_name': 'Wang',
    'Age': 28,
    'City': 'Yokohama'
}

person_info2 = {
    'First_name': 'Ryan',
    'Last_name': 'Wang',
    'Age': 27,
    'City': 'Tokyo'
}

person_info3 = {
    'First_name': 'Jack',
    'Last_name': 'Wang',
    'Age': 26,
    'City': 'Kyoto'
}

people = [person_info1, person_info2, person_info3]

for person in people:
    print(f"Name: {person['First_name']} {person['Last_name']}")
    print(f"\tAge: {person['Age']}")
    print(f"\tLocation: {person['City']}")

6.8
pet1 = {
    'type': 'dog',
    'owner': 'ryan'    
}

pet2 = {
    'type': 'bird',
    'owner': 'rose'    
}

pet3 = {
    'type': 'cat',
    'owner': 'jack'    
}

pets = [pet1, pet2, pet3]
for pet in pets:
    for key, value in pet.items():
        print(f"{key} : {value}")

#6.9
favorite_places = {
    'Ryan': ['Paris', 'Tokyo', 'Shanghai'],
    'Jack': ['London'],
    'Rose': ['New York', 'Beijing']
}

for name, places in favorite_places.items():
    print(f"Name: {name.title()}")
    print(f"Favorite places: ")
    for place in places:
        print(f"\t{place}")

#6.10
favorite_number = {
    'Ryan': [1,3,5],
    'Wang': [2,4,6],
    'Yi': [3,4,5],
    'Jack': [4,5,6]
}
for name, numbers in favorite_number.items():
    print(f"Name: {name.title()}")
    for number in numbers:
        print(number)

#6.11
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 10_000_000,
        'fact': 'Japanese capital'
    },

    'Beijing': {
        'country': 'China',
        'population': 20_000_000,
        'fact': 'Chinese capital'
    },
    
        'Lodon': {
        'country': 'UK',
        'population': 30_000_000,
        'fact': "UK's capital"
    },
}

for city, city_info in cities.items():
    print(f"The city is : {city.title()}")
    for key, value in city_info.items():
        print(f"\t{key} : {value}")
