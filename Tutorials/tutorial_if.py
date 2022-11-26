# #条件测试
# cars = ['bmw', 'Audi', 'Benz']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# #检查值是否相等！=
# requested_topping = 'mashrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies")

#数值比较
# age = 18
# if age != 17:
#     print(age, False)

#检查多个条件
#and: 都T则为T
#or：一个为T则为T

#检查特定条件 in
# requested_topping = ['mushrooms', 'onions', 'pineapple']
# if 'apple' in requested_topping:
#     print(True)
# else:
#     print(False)

#if-elif-else
# age = 12
# if age<4:
#     print("free")
# elif age<18:
#     print("25$")
# else:
#     print("40$")

#if处理列表
avaliable_toppings = ['mushrooms', 'olivers', 'green peppers', 'pepperoni', 
'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', ' french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print (f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")