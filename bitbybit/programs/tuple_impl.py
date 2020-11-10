"""
Tuple
--- Very Similar to lists
--- Index Based Operations Allowed
--- Holds homogeneous + hetrogeneous data elements (For Hetro Every element is treated as Object)
--- Immutable Cannot be Changed
--- Sequence Order is Preserved
--- Duplicates are Allowed
--- Multiple None Type Allowed

--- Tuple_methods: count, index
"""


# syntax: <name_for_tuple> = (element1, element2, element3,....,elementn)
#         <name_for_tuple> = tuple([element1,element2,....,elementn])

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

weekdays[0] = "new day"
print(weekdays)




# count = weekdays.count("Tuesday")
#
# print(count)
#
# index = weekdays.index("Wednesday")
# print(index)
#
#
# print(len(weekdays))

