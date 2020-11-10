"""Tuple
--- Very Similar to lists
--- Index Based Operations Allowed
--- Holds homogeneous + hetrogeneous data elements (For Hetro Every element is treated as Object)
--- Immutable Cannot be Changed
--- Sequence Order is Preserved
--- Duplicates are Allowed
--- Multiple None Type Allowed

--- Tuple_methods: count, index
"""

# ---------------------------------------------------------------------------

# syntax: <name_for_tuple> = (element1, element2, element3,....,elementn)
#         <name_for_tuple> = tuple([element1,element2,....,elementn])


weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', (1,2,3))

# ---------------------------------------------------------------------------

# Searches the Give Element and Return the Index position of that Element if present
# index = weekdays.index('Thursday')
# print(index)
# print("Index od thursday", weekdays.index('Thursday'))
#
# # ---------------------------------------------------------------------------
#
# # Returns the number of times a specified value occurs in a tuple
# count = weekdays.count('Tuesday')
# print(count)
# print("count of Tuesday", weekdays.count('Tuesday'))
#
# # ---------------------------------------------------------------------------
# # Length of tuple
#
# length = len(weekdays)
# print(length)
# print("Total days in week are:-", length)


# ---------------------------------------------------------------------------
# print(weekdays)
#
# weekdays[-1][2]=55
# print(weekdays)


