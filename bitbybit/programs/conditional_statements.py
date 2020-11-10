sample_list = [0]
months = ("jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sept", "oct", "nov", "dec")
message = ""
my_preferences = {'fruit': 'pomegranate', 'bike': 'honda', 'cuisine': 'indian', 'weather': 'winter', 'sport': 'cricket'}

# if condition:
#     block

# if condition:
#     block
# else:
#     block

# if condition:
#     block
# elif condition:
#     block
# elif condition:
#     block
# else:
#     block


if sample_list:
    print("list has some elements")

if not message:
    print("goodd morning")

#
# if 10==20:
#     print("condition is true")
# else:
#     print("condition is false")
#
# if 21==20:
#     print("first condition is true")
# elif 21<20:
#     print("second condition is true")
# else:
#     print("all condditions are false")


if 'jan' in months:
    print("jan is present")

if 'bike' in my_preferences.keys():
    print(my_preferences['bike'])

# x = int(input())
#
# if x==1:
#     print("1")
# elif x==2:
#     print("2")
# elif x==3:
#     print("3")
# else:
#     print("we don't have that option")

x = 5
y = 5

if x is y:
    print("true")