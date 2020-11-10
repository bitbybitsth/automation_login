

message_1 = "hello guys"
message_2 = "gooD mooRning"
message_3 = "email10"
message_4 = "9766588937"
message_5 = "**username@gmail.com**"
message_6 = "Ice cream, I scream, you scream, we all scream for ice cream!"


# concatination
#
# message_7 = message_1+message_2
# print(message_7)


# capitalize(), Capitalize first alphabet of string
# print("capitalize string:", message_1.capitalize())

# center(width, fillchar), width is total width of string, fillchar , character to fill gaps

# print("using Center:-", message_1.center(50, '*'))


# find(substring, start, end) returns start_index of substring if found, else -1
#
# result = message_2.find("oo", 4, 8)
# print(result)
# result = message_2.find("oo", 5)
# print(result)

# index(substring, start, end), similar to find() but raises a ValueError if substring not found
# result = message_2.index("oo")
# print(result)
# print(message_2.index("ooo"))


# # count(substring, start, end) start end optional, returns count

# result = message_2.count("ooo", 1, 6)
# print(result)

# endswith(suffix, start, end), return True if the string ends with given suffix, else False

# print("message ends with ing:", message_2.endswith('ing'))
# print("message ends with ing:", message_3.endswith('ing'))

# startswith(prefix, start, end), return True if the string starts with given prefix, else False

# print("message starts with good:", message_1.startswith("good"))
# print("message starts with good:", message_2.startswith("good"))



# isalnum(), return True if string contains only number & alphabets
#
# print("is string an alphanumneric", message_3.isalnum())
# print("is string an alphanumneric", message_2.isalnum())
#
# isalpha(), return True if string contains only alphabets, no symbols, no space,
# print(message_3.isalpha())
# print(message_2.isalpha())

# isdigit() , return True if string contains only digits, else False

# print(message_3.isdigit())
# print(message_4.isdigit())

# swapcase() , swaps the cases in string

# print(message_2.swapcase())

# split(char) = splits the string into list of strings by the given char"
#
# split_list = message_2.split(" ")
# print(split_list)
#
# split_list = message_5.split("@")
# print(split_list)
#
# sample_st = "home/pgosavi/Music/programs/venv/bin/python /home/pgosavi/Music/programs/string_implementation.py"
# split_list = sample_st.split("/")
# print(split_list)

# print("original string:-", message_5)
# print("stripped string:-", message_5.strip('*'))


# replcae(oldstrong,new string, count) , replaces old string with new string for specified no of count.

print("original string:-", message_6)
print("stripped string:-", message_6.replace("scream", "shout", 2))
