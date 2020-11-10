# """"
# List:
# --- Backed by Array
# --- Index Based  - start from 0 - Index can be Positive and Negative - Positive Index >=0 , Negative Index <=-(Length)
# --- Eg: a[-2] is actually a[length-2]
# --- Holds homogeneous + heterogeneous data elements
# --- Mutable - can append/add/replace/remove/update
# --- Sequence Order is Preserved
# --- Duplicates are Allowed
# --- Multiple None Type Allowed
# --- Ideal for searching and retrieval
# --- Insertion and Deletion are costly operations
#
# --- List_methids = append, insert, extend , copy , count, reverse, pop, remove, sort, index, clear
# """
#
#
# # Syntax <name_for_List> = [Elements separated with Comma in Square Bracket]
# #  <name_for_list> = list(Elements separated with Comma)
#
list_of_denominations = [1, 2, 5, 10, 50, 20, 50, 100, 500, 1000]
# # print('\nGiven Denominations Data:', list_of_denominations)
#
# # # -------------------------------------------------------------------------------------
# # # Print all items in the list one by one
# # print('Printing list one by One')
# # for denomination in list_of_denominations:
# #     print(denomination)
#
# # # -------------------------------------------------------------------------------------
# # No of Items in the list
#
# # print(len(list_of_denominations))
#
# # # -------------------------------------------------------------------------------------
#
# # index(element), return the eindex ofgiven eleemnt, takes element as input parameter
#
# # index = list_of_denominations.index(500)
# # print(index)
#
# # # -------------------------------------------------------------------------------------
#
# # Append(element) : append is used to add an element at the last position of list, takes elements as input.
#
# list_of_denominations.append(2000)
# # print(list_of_denominations)
#
# # # -------------------------------------------------------------------------------------
# # insert(index, element) - insert used to add an element in between
# # list_of_denominations.insert(8, 200)
# # print(list_of_denominations)
#
# # # -------------------------------------------------------------------------------------
# # Extend(list) : extend is used appned  a list to existing list, takes list as argument
#
# # digital_currency = ['gPay', 'PhonePay', 'PayTm']
# list_of_denominations.extend(['gPay', 'PhonePay', 'PayTm'])
# # print(list_of_denominations)
#
# # list_of_denominations += [250, 300]
# # print(list_of_denominations)
#
# # # -------------------------------------------------------------------------------------
# # copy() : returns copy of the list where the function is used
# # copy_list = list_of_denominations.copy()
# #
# #
# # print("original", list_of_denominations)
# # print("copied", copy_list)
# # copy_list.append(600)
# # print("copied", copy_list)
# # print("original", list_of_denominations)
#
#
# # copy_list = list_of_denominations
# # print("original", list_of_denominations)
# # print("copied", copy_list)
# # copy_list.append(600)
# # print("copied", copy_list)
# # print("original", list_of_denominations)
#
# # print("copied", copy_list)
# # copy_list = list_of_denominations
# # copy_list.append([300, 400])
# # print("copied", copy_list)
# # print("original", list_of_denominations)
#
# # # -------------------------------------------------------------------------------------
#
# # count(element)  given element's count in list
#
# # count = list_of_denominations.count(50)
# # print(count)
#
#
# # # -------------------------------------------------------------------------------------
# # reverse() : reverses the given list
#
# # list_of_denominations.reverse()
# # print(list_of_denominations)
#
# # # # -------------------------------------------------------------------------------------
# # print("original", list_of_denominations)
# last_element = list_of_denominations.pop()
# #
# # print("Popped element", last_element)
# # print("original", list_of_denominations)
# print("Popped element", list_of_denominations.pop())
# # print("original", list_of_denominations)
# print("Popped element", list_of_denominations.pop())
# # print("original", list_of_denominations)
#
# # # # -------------------------------------------------------------------------------------
# # remove(element) :  remove function removes given element
# # print("original", list_of_denominations)
# list_of_denominations.remove(1000)
# # print(list_of_denominations)
#
# # # # -------------------------------------------------------------------------------------
# print("original", list_of_denominations)
# list_of_denominations.sort(reverse=True)
# list_of_denominations.sort()
# print(list_of_denominations)
#
#
# # print("orignal", list_of_denominations)
# # sorted_List = sorted(list_of_denominations, reverse=True)
# # print("sorted", sorted_List)
# # print("original", list_of_denominations)
#
#
# # # # -------------------------------------------------------------------------------------
# #
# # list_of_denominations.clear()
# # print(list_of_denominations)
# #
# # list_of_denominations.append(400)
# # print(list_of_denominations)
#
#
#
#
# another_reference = list_of_denominations.copy()
# list_of_denominations.clear()
# print(list_of_denominations)
# print(another_reference)
#
#

# for counter, item in enumerate(list_of_denominations):
#     print(f"{item} present at position {counter}")

# x = {key:val for val, key in enumerate(list_of_denominations,10)}
# print(x)


