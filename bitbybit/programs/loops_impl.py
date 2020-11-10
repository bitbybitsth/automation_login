# for loop -
# while loop -
# for else loop
# while else loop
# expanded for loop
# list comprehension
# dict comprehension





sample_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, "jan", 1024, 2048]
months = ("jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sept", "oct", "nov", "dec")
message = "Good Morning"
my_preferences = {'fruit': 'pomegranate', 'bike': 'honda', 'cuisine': 'indian', 'weather': 'winter', 'sport': 'cricket'}

message_list = list(message)
print(message_list)


#
# sum = 0
# for number in sample_list:
#     sum += number
#
# print(sum)
#
#
# x = []
# for month in months:
#     x.append(month.upper())
#
# y = tuple(x)
# print(y)
#
#
# for key, value in my_preferences.items():
#     print(key)
#     print(value)





#
# counter = 0
# # sum = 0
#
for item in sample_list:
    # sum +=item
    if item in months:
        break
    print(item)
else:
    print("none of the items of samplelist is present in months")



# x = [x for x in range(400,500) if x%10==0]
# print(x)

# y = {key:chr(key) for key in range(65,90)}
# print(y)
#
# z = {item for item in sample_list if item}
# print(z)
# z = set(sample_list)
# print(type(z))


x = [item if item%2==0 else "Odd" for item in range(1,20) ]
print(x)

x = input("enter a number")
for char in x:
    print("x is greater than 0")









#
# for month in months:
#     if month == "may":
#         print("happy workers day")
#     else:
#         print(month)

# for key, value in my_preferences.items():
#     print(key)
#     if key == "bike":
#       print("my fav bike is honda")
#     elif key=="cuisine":
#         print("i like indian food")
#     elif key == "sport":
#         print("i like to watch crciket")

# print("Enter no of iterations")
# n = int(input())
#
# fib_list = [0,1]
# i=0
# j=1
#

# def fib_func(n,fib_list):
#     i=0
#     j=1
#     while True:
#         if n <= 0:
#             break
#         fib_list.append(fib_list[i] + fib_list[j])
#         i += 1
#         j += 1
#         n -= 1
#     else:
#         print("10 Fibonacci numbers displayed successfully")
#
#     return fib_list

# result = fib_func(10,[0,1])
# print(result)
#
#
new_list = [x for x in range(1, 10)]

blank_link = []

for x in range(1,10):
    blank_link.append(x)

new_list = blank_link
#
# new_dict = {item:index for index,item in enumerate(sample_list)}
#
# print(new_dict)
# print(type(new_dict))
#
# def f1():
#     pass
#
def f2():

    pass

def f3():
    pass
#
#
#
# def f4(x):
#     if x==10:
#         pass
#     else:
#         for i in range(1,10):
#             print("***")
#             if i%2==0:
#                 pass
#             print(f"i = {i}")
#
#
#
# f4(11)
# f3()


#
# num = [x for x in range(1, 7)]
# mul = [x for x in range(1, 11)]
#
# print(num)
# print(mul)

# for n in num:
#
#     break
#     print("")
#     for m in mul:
#         # if m%6==0:
#         #     continue
#         print(f"{n} * {m} = {n*m}")



#
#
#
#
#
#
#
#
#
#
