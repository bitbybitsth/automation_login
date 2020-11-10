"""
dict
 --- internally implemented as hashtable and uses closed hashing  a.k.a open addressing
 --- 8 address location allocated in memory
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


# Syntax <name_for_dict> = {key1:value1, key2:value2,....,keyn:valuen}
#  <name_for_list> = dict({key1:value1, key2:value2,....,keyn:valuen})

my_preferences = {'fruit': 'pomegranate', 'bike': 'honda', 'cuisine': 'indian', 'weather': 'winter', 'sport': 'cricket'}
print(my_preferences)


# # items() method is used to return the list with Key, value pair as tuple
# print("Items in Dictionary:-", my_preferences.items())
# items = my_preferences.items()
# print(items)

# # keys(), return a list of all keys.
# key_list = my_preferences.keys()
# print(key_list)

# # values() , return's all the values in the dictionary
# values = my_preferences.values()
# print(values)

# # get(key), return the value of the key given
# val = my_preferences.get("bike")
# print("Bike's value", val)
# val = my_preferences.get("car", "hero")
# print("Bike's value", val)
#
# val = my_preferences["bike"]
# print(val)

# # fromkeys(sequencetype, optional_default_value) ,  create a dictionary from the sequence given

# seq_list = ("mon", "tue", "wed")
# new_dict = dict.fromkeys(seq_list, "day of the week")
# print(new_dict)


# setdefault(key,optional_default_value), returns value of key if key is present.
# adds key to dict if key not present, if default_value is given the value is set with key or else None is set

# value = my_preferences.setdefault("bike")
# print(value)
# value = my_preferences.setdefault("country", "india")
# print(value)
# print(my_preferences)


# update(), used to update an existing dict with new dict

# new_dict = {"state": "maharashtra", "city": "solapur/pune"}
# my_preferences.update(new_dict)
# print(my_preferences)


# # pop() removes and key,value of the key from dictionary and return the value
# # & popitem() randomly pops an item from  dictionary
#
# element = my_preferences.pop("bike")
# print(element)
# print(my_preferences)
# item = my_preferences.popitem()
# print(item)
# print(my_preferences)
# item = my_preferences.popitem()
# print(my_preferences)

# copy() : creates a shallow copy of dictionary
#
# copy_dict = my_preferences.copy()
# copy_dict.update({"car": ["honda", "hundayi"]})
#
# print(copy_dict)

# # clear() , clears the dict
# my_preferences.clear()
# print(my_preferences)