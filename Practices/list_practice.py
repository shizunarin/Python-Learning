#3.1
names = ['cat', 'dog', 'bird', 'flower']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3.2
message = "Your name is: " 
print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])

#3.4
guests = ['Tom', 'Jack', 'Ryan', 'Rain']
message = "Would you like to have dinner with me? "
print(message + ', ' + guests[0] + ', '+ guests[1] + ', '+ guests[2] + ', '+ guests[3])

#3.5
popped_guests = guests.pop(-1)
print("I just heard " + popped_guests + " can not join us")
guests.append('Rose')
print(message + ', ' + guests[0] + ', '+ guests[1] + ', '+ guests[2] + ', '+ guests[3])

#3.6
guests.insert(0, 'Wang')
guests.insert(3, 'Zhang')
guests.append('Yang')
for name in guests:
    print("We inveted those guys ot our party: " + name)
print(len(guests))

#3.7
print("Sorry we could just invite two guests to join our partu")
print(guests.pop() + " Sorry for cancel your party!")
print(guests.pop() + " Sorry for cancel your party!")
print(guests.pop() + " Sorry for cancel your party!")
print(guests.pop() + " Sorry for cancel your party!")
print(guests.pop() + " Sorry for cancel your party!")

del guests[1]
del guests[0]

print(guests)

3.8
places = ['Tokyo', 'Pairs', 'Shanghai', 'New York', 'London']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

