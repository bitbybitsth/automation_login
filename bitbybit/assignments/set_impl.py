"""
set
--- Backed by Hashtable - Open address a.k.a closed hashing
--- No Index Based Operations Allowed
--- Holds homogeneous + heterogeneous data elements (For Hetro Every element is treated as Object)
--- sets are Mutable - can add/remove/update
--- but the elemnts of set should be immutable
--- Sequence Order is Not Preserved
--- Duplicates are not Allowed
--- Single None Type Allowed
--- Ideal for Insertion and Deletion
--- Searching and retrieval might be costly operations


--- Set methods: add, clear, copy, pop, remove, difference, difference_update, discard, intersection, intersection_update,
    isdisjoint, issubset, issuperset, symmetric_difference, symmetric_difference_update, unioun, update.
"""

# --------------------------------------------------------------------------------
# syntax <name_for_set> = {element, element, element,...,element}
#        <name_for_Set> = set([element, element, element])
#
set_1 = {10, 20, 30, 40, 50, 50, 40}
set_2 = set([40, 50, 60, 70, 80, 60, 40])
print(set_1)
print(set_2)
#
#
#
# # ----------------------------------------------------------------------------------
#
# # s1.union(s2) : return a union set of calling set and passed set (s1 union s2)
# union_set = set_1.union(set_2)
# print("union of set1 & set2 is:", union_set)
#
# # ----------------------------------------------------------------------------------
#
# # s1.intersection(s2) : return a intersection set of calling set and passed set (s1 intersection s2)
# intersection_set = set_1.intersection(set_2)
# print("intersection of set1 & set2 is:", intersection_set)
#
# # s1.intersection_update(s2) : assigns the intersection of calling set and passed set to calling set
# set_1.intersection_update(set_2)
# print(set_1)
#
# # ----------------------------------------------------------------------------------

# # s1.difference(s2) : return a difference between calling set and passed set s1 - s2
# diff_set = set_1.difference(set_2)
# print("difference between set1 & set2 is:", diff_set)
#
# diff_set = set_2.difference(set_1)
# print("difference between set2 & set1 is:", diff_set)
#
# set_1.difference_update(set_2)
# print(set_1)
#
# # ----------------------------------------------------------------------------------

# # s1.symmetric_difference(s2) : return a symmetric difference of calling set and passed set
# symm_diff_set = set_1.symmetric_difference(set_2)
# print("symmetric difference is of set1 & set2 is:", symm_diff_set)
#
# set_1.symmetric_difference_update(set_2)
# print(set_1)
#
# ----------------------------------------------------------------------------------
#
# s1.issubset(s2) : return a True if calling set is a subset of passed set, else returns False
# set_3 = {10, 20}
# sub_set = set_3.issubset(set_1)
# print("set3 is  subset of set1:", sub_set)
# sub_set = set_3.issubset(set_2)
# print("set3 is  subset of set2:", sub_set)
#
# ----------------------------------------------------------------------------------
#
# s1.issuperset(s2) : return a True if calling set is superset of passed set, else returns False
# set_3 = {10, 20}
# super_set = set_1.issuperset(set_3)
# print("set1 is  superset of set3:", super_set)
# super_set = set_2.issuperset(set_3)
# print("set2 is  superset of set3:", super_set)
#
# ----------------------------------------------------------------------------------
# s1.isdisjoint(s2) : return a True if both sets are disjoint, i.e they don't have any elements common between them
#
# print("set1 & set2 are disjoint:", set_1.isdisjoint(set_2))
#
# ----------------------------------------------------------------------------------

# add() : adds a element to set if not preset
#
# set_2.add(100)
# set_2.add(50)
# print(set_2)
#
# ----------------------------------------------------------------------------------

# update() ,  used to combine 2 sets to 1

# set_1.update(set_2)
# print(set_1)
# set_1.update([90, 100])
# print(set_1)
#
# ----------------------------------------------------------------------------------
# pop() , removes and returns a random element from set.
#
# element = set_1.pop()
# print(element)
# print(set_1)
#
# ----------------------------------------------------------------------------------

# discard() & remove()

# discard(element) : used to discard/deletes and element from set
#
# set_1.discard(20)
# print(set_1)

# remove(element): used to remove/delete and element from set

# set_1.remove(20)
# print(set_1)

# ----------------------------------------------------------------------------------

# copy() - to cpy the set

# set_3 = set_1.copy()
# print(set_3)

# ----------------------------------------------------------------------------------

# set_1.clear()
# set_2.clear()
#
# print(set_2)
