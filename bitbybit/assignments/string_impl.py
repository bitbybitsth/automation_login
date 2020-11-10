message_1 = "hello guys"
message_2 = "good mooRning"
message_3 = "email10"
message_4 = "9766588937"
message_5 = " username@gmail.com "
message_6 = "Ice cream, I scream, you scream, we all scream for ice cream!"

# Concatination
# result = message_1 + message_2
# print(result)
#
# capitalize() captalize the first letter
# print(message_1.capitalize())
#
#
# center(width, fillchar)
#
# result = message_1.center(20)
# print(result)
#
# find(substring, start, end) returns start_index of substring if found, else -1
#
# result = message_2.find("oo")
# print(result)
# result = message_2.find("oo", 5)
# print(result)
# # index(substring, start, end), similar to find() but raises a ValueError if substring not found
# result = message_2.index("oo")
# print(result)
# print(message_2.index("ooo"))


#
# # count(substring, start, end) start end optional, returns count
# count = message_2.count("oo")
# print(count)
# count = message_2.count("oo", 5, 8)
# print(count)
#
# # endswith(suffix , start, end), return True or False
#
# ends_with_ing = message_2.endswith("ing")
# print(ends_with_ing)
# ends_with_ing = message_2.endswith("ing", 5, 11)
# print(ends_with_ing)
#
# # startswith(prefix, start, end)
# starts_with_good = message_2.startswith("good")
# print(starts_with_good)
# starts_with_good = message_2.startswith("good", 0, 2)
# print(starts_with_good)

# isalnum(), return True if string contains only number & alphabets

# print(message_3.isalnum())
#
# isalpha(), return True if string contains only alphabets, no symbols, no space,
# print(message_3.isalpha())
# print(message_2.isalpha())

# isdigit() , return True if string contains only digits, else False

# print(message_3.isdigit())
# print(message_4.isdigit())

# swapcase(), returns string with cases swapped of every character
# result = message_2.swapcase()
# print(result)

# split(spllit_char), splits the string by given char, returns a list with values after split
# result = message_5.split("@")
# print(result)

# strip(), returns a string with charcters removed from start and end, default char " "
# print(message_5)
# result = message_5.strip()
# print(result)

# replace(old_substring, new_substring,count)
# # returns the replaced string if replacement is done, else returns original string
# # if count give replaces the substring for no of count , else replaces all occurrences
# replaced_string = message_6.replace("scream", "shout")
# print(replaced_string)


# https://www.programiz.com/python-programming/methods/string