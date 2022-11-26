#遍历列表
magicians = ['alice', 'davide', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
print("Thanks everyone, that's todays show")

#创建数值列表 range()
for value in range(6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_number = list(range(2,11,2))
print(even_number)

# 列表数值的平方
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)# or squares.append(value ** 2)
print(squares)

#最大，最小，求和
digits = [1,2,3,4,5,6,7,8,9,10]
print(max(digits))
print(min(digits))
print(sum(digits))

#列表解析
squares = [value ** 2 for value in range(1,11)]
print(squares)

#列表的一部分
#遍历切片
players = ['player1', 'player2', 'player3','player4', 'player5']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#复制列表
my_player = players[:]
print(my_player)
players.append('player6')
my_player.append('player7')
print(players)
print(my_player)

#元祖 (不能修改的值，称为不可变的， 不可变的列表称为元祖)
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] =250 --error 元组值不能修改
print(dimensions[0])

for dimension in dimensions:
    print(dimension)

#修改元组变量
dimensions = (400, 50)
for dimension in dimensions:
    print(dimension)

