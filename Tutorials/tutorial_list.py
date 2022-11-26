bicycles = ['trek', 'cannonadale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[1])
print(bicycles[-1])#负数表示链表的最后一位数值，可以在不确定长度的情况下反向索引

#修改，添加，删除元素
cars = ['honda', 'toyota', 'suzuki', 'yamaha']
print(cars)

cars[0] = 'ducait'
print(cars)

cars.append('dicait')#add element
print(cars)

cars.insert(0,'bbb')
print(cars)

del cars[0]
print(cars)

popped_car = cars.pop(0)
print(cars)
print(popped_car)

cars.remove('honda')
print(cars)

#排序
cars.sort()
print(cars)

cars.sort(reverse=True)#按字母倒序
print(cars)

print("After sort: " + str(sorted(cars)))
print("The original list: " + str(cars))

cars.reverse()
print(cars)

#链表长度
print(len(cars))
