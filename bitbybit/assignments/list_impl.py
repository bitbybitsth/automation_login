"""Lists ---
--- Backed by Array
--- Index Based  - start from 0 - Index can be Positive and Negative - Positive Index >=0 , Negative Index <=-(Length)
--- Eg: a[-2] is actually a[length-2]
--- Holds homogeneous + heterogeneous data elements
--- Mutable - can append/add/replace/remove/update
--- Sequence Order is Preserved
--- Duplicates are Allowed
--- Multiple None Type Allowed
--- Ideal for searching and retrieval
--- Insertion and Deletion are costly operations

--- List_methods = append, insert, extend , copy , count, reverse, pop, remove, sort, index, clear
"""
# # -------------------------------------------------------------------------------------
#
# Syntax <name_for_List> = [Elements separated with Comma in Square Bracket]
#  <name_for_list> = list(Elements separated with Comma)


list_of_denominations = [1, 20, 50, 10, 5, 2, 50, 100, 500, 1000]
print('\nGiven Denominations Data:', list_of_denominations)
# print(list_of_denominations[-1])
# print(list_of_denominations[-5])
#
# # -------------------------------------------------------------------------------------
#
# Print all items in the list one by one
# print('Printing list one by One')
# for denomination in list_of_denominations:
#     print(denomination)


# # -------------------------------------------------------------------------------------
#
# No of Items in the list

# print(len(list_of_denominations))
#
# # -------------------------------------------------------------------------------------
#
# index = list_of_denominations.index(500)
# print('500 is at index =', index)
#
#
# # -------------------------------------------------------------------------------------
#
# Append on List - Adds the parameter_content to the end of the list
# list_of_denominations.append(2000)
# print('\nAppended New Highest Currency:', list_of_denominations)
#
#
# # -------------------------------------------------------------------------------------
#
# insert in between - First param is Index position - second is the element to inserted
#
# list_of_denominations.insert(8, 200)
# print('\nInserted New Currency:', list_of_denominations)
#
# # -------------------------------------------------------------------------------------
#
# Extend Adds a list starting from the last position
# digital_currency = ["gPay", "PhonePay", "PayTm"]
# list_of_denominations.extend(digital_currency)
# # list_of_denominations.append(digital_currency)
# print('\nExtended the List with Digital Currency:', list_of_denominations)
#
# list_of_denominations += [250, 400]
# print(list_of_denominations)

#
#
# # --------------------------------------------------------------------------------------
#
# #  Copy Returns a Copy
# list_of_denominations_copy = list_of_denominations.copy()
# print('Copy of Existing List:', list_of_denominations_copy)
# # list_of_denominations_copy.append("gPay")
# #
# # print(list_of_denominations_copy)
# # print(list_of_denominations)
#
#
# # -------------------------------------------------------------------------------------
#
# # Counts no of time the given element is present
# count = list_of_denominations.count(50)
# print(count)
# print('\nNo OF Time given element 500 is present:', list_of_denominations.count(500))
#
# # -------------------------------------------------------------------------------------
#
# to reverse the list
# list_of_denominations.reverse()
# reversed_list = list_of_denominations[-1::-1]
# print(reversed_list)
# # print(list_of_denominations)
# print('\nReversed List:', list_of_denominations)
# print(id(list_of_denominations) == id(list_of_denominations))
# list_of_denominations.reverse()
#
# # -------------------------------------------------------------------------------------
#
# pops out the last element in the list
# last_element = list_of_denominations.pop()
# print(f'Last Element {last_element} Removed')
# print(f'Last Element {list_of_denominations.pop()} Removed')
# print(f'Last Element {list_of_denominations.pop()} Removed')
# print(list_of_denominations)
# # #
# # # # -------------------------------------------------------------------------------------
# # #
# # # Remove the given element if present
# list_of_denominations.remove(1000)
# print('\n Banned Currency Removed:', list_of_denominations)
#
# # -------------------------------------------------------------------------------------
#
#
# # Sorting List -
# # Sorting in list works only if the list has homogenous elements, i.e. list must contain same type of elements
# # list sorting will not work on list with dictionary as elements will raise an error, while with set doesn't raise and error but nothing affects the list
#
# # Sorts in Descending order
# list_of_denominations.sort(reverse=True)

# new_list = sorted(list_of_denominations,reverse=True)
# print(list_of_denominations)
# print(new_list)
#
# print('Sorted List Type 2:', list_of_denominations)

# # Sorts in Ascending order
# list_of_denominations.sort()
# print(list_of_denominations)
# # new_list = sorted(list_of_denominations)
# # print(new_list)
# print('\nSorted List Type 1:', list_of_denominations)
# -------------------------------------------
#
#
# # # Clears the list
# list_of_denominations.clear()
# print('\n List Cleared:', list_of_denominations)
# list_of_denominations.append(300)
# print(list_of_denominations)
# #
# # -------------------------------------------------------------------------------------

# x = list_of_denominations[0:5]
# print(x)
