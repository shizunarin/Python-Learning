5.1
car = 'audi'
print(car == 'bmw')

5.3
alien_color = 'green'
if alien_color == 'green':
    print("player got 5 points")

alien_color = 'red'
if alien_color == 'green':
    print("player got 5 points")

5.4
alien_color = 'green'
if alien_color == 'green':
    print("You got 5 points because you killed a alien")
else:
    print("You got 10 points")


alien_color = 'green'
if alien_color != 'green':
    print("You got 5 points because you killed a alien")
else:
    print("You got 10 points")

5.5
alien_color = 'green'
if alien_color == 'green':
    print("You got 5 points.")
elif alien_color == 'yellow':
    print("You got 10 points.")
else:
    print("You got 15 points")

alien_color = 'yellow'
if alien_color == 'green':
    print("You got 5 points.")
elif alien_color == 'yellow':
    print("You got 10 points.")
else:
    print("You got 15 points")

alien_color = 'red'
if alien_color == 'green':
    print("You got 5 points.")
elif alien_color == 'yellow':
    print("You got 10 points.")
else:
    print("You got 15 points")

5.6
age = 10
if age < 2:
    print("Baby")
elif age < 4:
    print("Child")
elif age < 13:
    print("Junior")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
elif age >= 65:
    print("Older")

5.7
favorite_fruits = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'melon' in favorite_fruits:
    print("You really like melon")
if 'pear' in favorite_fruits:
    print("You really like pear!")

5.8
user_list = ['admin', 'Jordan', 'user1', 'user2', 'user3']

for user in user_list:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for your logging in again")

5.9
user_list = ['admin', 'Jordan', 'user1', 'user2', 'user3']

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for your logging in again")
else:
    print("We need find some users!")


user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for your logging in again")
else:
    print("We need find some users!")

5.10
current_users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
new_users = ['user1', 'user2', 'user7', 'user8', 'user9']

for user in new_users:
    if user.lower() in current_users:
        print("User name existed, please input another username")
    else:
        print("Username avaliable!")

5.11
number_list = list(range(1,10))

for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
