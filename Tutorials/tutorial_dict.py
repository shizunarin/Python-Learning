#Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#using Dictionary
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Add key value pairs 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#modify the value of dict
alien_0 = {'color': 'green'}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {
    'color': 'green', 
    'points': 5, 
    'x_position': 0, 
    'y_position': 25,
    'speed': 'medium'
    }

if alien_0['speed'] == 'slow':
    x_increament = 1
elif alien_0['speed'] == 'medium':
    x_increament = 2
elif alien_0['speed'] == 'high':
    x_increament = 3

alien_0['x_position'] = alien_0 ['x_position'] + x_increament

print(f"New position is {alien_0['x_position']}")

#Delete the key value paris 
alien_0 = {
    'color': 'green', 
    'points': 5, 
    'x_position': 0, 
    'y_position': 25,
    'speed': 'medium'
}

del alien_0['x_position']
del alien_0['y_position']
del alien_0['speed']
print(alien_0)

#similar objective
favorite_languages = {
    'jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(f"Sarah's favorite language is {favorite_languages['Sarah']}")

# Using get()
alien_0 = {
    'color': 'green', 
    'points': 5, 
}

# print(alien_0['speed'])
print(alien_0.get('speed', 'No value assigned'))
print(alien_0.get('speed'))

# Traverse Dict
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key,value in user_0.items():
    print(f"\n{key}")
    print(f"{value}")

#Traverse key()
favorite_languages = {
    'jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print(f"Hi {name}!, I see you love {favorite_languages[name]}")

#Traverse all values
favorite_languages = {
    'jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned: ")
# for language in favorite_languages.values():#未考虑重复项，如果考虑重复项，需要用集合set()
for language in set(favorite_languages.values()):
    print(language.title())

#Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print("Total number of aliens: {}".format(len(aliens)))
#if-elif-else修改值,etc

#Store list in dict
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You orderd a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

#list in dict
favorite_languages = {
    'jen': ['python', 'ruby'],
    'Sarah': ['c'] ,
    'edward': ['ruby', 'go'],
    'phil': ['python', 'hasekell'],
    'yi': []
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is : ")
        for language in languages:
            print(f"\t {language.title()}")
    elif len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are : ")
        for language in languages:
            print(f"\t {language.title()}")
    else:
        print(f"\n{name.title()} dosen't have favorite language.")

#dict in dict
users = {
    'aeinstein':{
        'first': 'alebrt',
        'last': 'einstein',
        'location': 'Princeton',
    },

    'murie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'Paris'
    }
}

for username, user_infos in users.items():
    print(f"User name : {username}")
    print(f"\t Full name: {user_infos['first'].title()} {user_infos['last'].title()}")
    print(f"\t Loaction: {user_infos['location']}")

