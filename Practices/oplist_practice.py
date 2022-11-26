# 4.1
pizzas = ['pizza1', 'pizza2', 'pizza3']
for pizza in pizzas:
    print(f"I like {pizza.title()}")
print("I really love pizza!")

# 4.2
animals = ['cat', 'fish', 'dog']
for animal in animals:
    print(f"A {animal} would make a great pet")
print("Any of these animals would make greate pet!")

# 4.3
list = []
for number in range(1,21):
    list.append(number)
print(list)

# 4.4
numbers = list(range(1,1000001))
for number in numbers:
    print(number)

# 4.5
numbers = list(range(1,1000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4.6
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

# 4.7
divison_numbers = list(range(3, 31, 3))
for number in divison_numbers:
    print(number)

#4.8
triple_number = []
for number in range(1,11):
    triple = number ** 3
    triple_number.append(triple)
print(triple_number)

#4.9
triples = [number ** 3 for number in range(1,11)]
print(triples)

#4.10
pizzas = ['pizza1', 'pizza2', 'pizza3', 'pizza4', 'pizza5']
print(f"The first three items in the list are: {pizzas[:3]}")
print(f"Three items from the middle of the list are: {pizzas[1:4]}")
print(f"The last three items in the list are: {pizzas[-3:]}")

#4.11
friend_pizzas = pizzas[:]
pizzas.append('pizza6')
friend_pizzas.append('pizza7')
print(f"My favorite pizzas are : ")
for my_pizza in pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

# 4.13
foods = ('apple', 'banana', 'peal', 'orange', 'ramen')
for food in foods:
    print(food)

# foods[0] = 'water'

foods = ('apple', 'banana', 'peal', 'watermelen', 'bread')
for food in foods:
    print(food)