from datetime import datetime
# def function(**kwargs):
#     for key in kwargs.values():
#         print(f"{key} ->")
#
#
# function(a=10, b=20, c=30, d=40, e=50)



# print(x)
#
# # sequence_type[start:stop:step]
# y = x[:]
#
# y = {item:chr(item) for item in range(65,90)}
# print(y)
#
# print(x[100:50:-5])



# india = {"flag": "tricolour", "bird":"peacock", "animal": "tiger"}
#
# anthem = india.get("bird")
#
# if anthem:
#     print(anthem)
# z = [x for x in range(1,101)]
#
# x = input("Enter Choice")
#
# # if x%2 ==0:
# #     print("even")
# # else:
# #     print("odd")
#
# x = z[1::2] if x=="even" else z[0::2]
#
# print(x)

#
# message = "CLOSE ON the heels of consignments from China"
#
#
# x = message.replace("the", "THE")
# print(x)
#

#
# def format_date(dt):
#     dt = datetime.strptime(dt[0:19], "%Y-%m-%dT%H:%M:%S").strftime("%b %d %YT%H:%M:%S")
#     dt = dt.split('T')  # ['Jun 20 2020', '21:24:15']
#
#     hour = int(dt[1][0:2])
#
#     suffix = f" AM UTC" if hour < 12 else " PM UTC"
#
#     hour = (hour + 11) % 12 + 1 if hour > 12 else hour
#     time = dt[1].replace(dt[1][0:2], str(hour)) + suffix
#     formatted_date = dt[0] + " " + time
#     return formatted_date
#
# x = format_date("2020-06-27T20:40:15+0000")
# print(x)


x = input("Enter number")

if x.isdigit():
    pass
else:
    print("invalid number")




# print(x)


# vov = ['a', 'e', 'i', 'o', 'u']
#
#
# for item in x:
#     if item[0] in vov:
#         print(item)







# y = []
#
# for item in x:
#     if item%2!=0:
#         y.append(item)
#
# print(y)

# y = x[0::2]


# y = {key:chr(key) for key in range(65,91)}
#
# print(x)
# print(y)

