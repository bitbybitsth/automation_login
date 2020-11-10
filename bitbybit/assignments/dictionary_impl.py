"""
 dict
 --- internally implemented as hashtable and uses closed hashing  a.k.a open addressing
 --- Unlike other data types Dictionary holds a pair (KEY,VALUE) as a single element.
 --- Dictionary is mutable
 --- Key must be immutable(String, Number, Tuple) and no duplicates allowed.
 --- Value cannot be of any type(Mutable or immutable) and duplicated are allowed.
 --- elements are accessed using keys
 --- can be nested
 --- insertion deletion is efficient and searching is  not efficient compared to insertion/deletion.

 --- Dict_methods:
 --- copy(), clear(), fromkeys(), get(), items(), keys(), values(), pop(), popitem(), setdefault(), update()
"""
# # ---------------------------------------------------------------------------

# Syntax <name_for_dict> = {key:value, key:value, ..... ,key:value}
#

my_preferences = {'fruit': 'pomegranate', 'bike': 'honda', 'cuisine': 'indian', 'weather': 'winter', 'sport': 'cricket'}
# print(my_preferences)

# # ---------------------------------------------------------------------------
# items() method is used to return the list with Key, value pair as tuple
print("Items in Dictionary:-", my_preferences.items())
# items = my_preferences.items()
#
# for item in my_preferences.items():
#     print(item)
#
# # ---------------------------------------------------------------------------
# # keys() method is used to return the list with all dictionary keys.
# keys = my_preferences.keys()
# print("Keys of the dictionary are:-", keys)


# s = "bike"
# if "bike" in keys:
#     print()
#
# approved = ['fruit', 'bike', 'cuisine', 'weather']
#
# for key in my_preferences.keys():
#     if key in approved:
#         print(key)
#
# # ---------------------------------------------------------------------------
# values() method is used to return the list with all dictionary values.
# values = my_preferences.values()
# print(values)
#
# # ---------------------------------------------------------------------------
# get(key) , returns the value of given key

# bike = my_preferences.get("scooter", "TVS")
# print(bike)
# bike = my_preferences["scooter"]
# print(bike)
#
# # ---------------------------------------------------------------------------
# fromKeys(sequence_type, default_value)
# creates a dictionary from the sequence_type given, default value is None

# message = "hello"
# # new_dict = dict.fromkeys(message)
# # print(len(new_dict))
# # print(len(message))
# # print(new_dict)
# new_dict2 = dict.fromkeys(message, 10)
# print(new_dict2)
# phone_list = ["brand", "model", "price"]
# phone_dict = dict.fromkeys(phone_list, "sony")
# print(phone_dict)
# #---------------------------------------------------------------------------
# setdefault(key,optional_default_value), returns value of key if key is present.
# adds key to dict if key not present, if default_value is given the value is set with key or else None is set

# value = my_preferences.setdefault("bike")
# print(value)
# value = my_preferences.setdefault("scooter", "TVS")
# print(value)
# print(my_preferences)
# #---------------------------------------------------------------------------
# # update(), used to update an existing dict with new dict

# new_dict = {"state": "maharashtra", "city": "solapur/pune"}
# my_preferences.update(new_dict)
# print(my_preferences)
# #----------------------------------------------------------
# # pop() & popitem()
#
# value = my_preferences.pop("bike")
# print(value)
# print(my_preferences)
# value = my_preferences.pop("bike", False) # default value
#
# if value:
#     print("key is present")
# else:
#     print("key is not present")

# print(value)
# print(my_preferences)
# my_preferences.popitem()
# my_preferences.popitem()
# print(my_preferences)
#-----------------------------------------------------------------
# # copy() - copy

# copy_dict = my_preferences.copy()
# print(copy_dict)

# #---------------------------------------------------------------
# my_preferences.clear()
# print(my_preferences)
#










