##################### reverse ########################333
#
# x = "consolidate"
#
# # using slicing
# reversed_x = x[::-1]
# print(reversed_x)
#
# # using for loop
#
# y = "incorporate"
#
# reversed_y = ""
# for item in y:
#     reversed_y = item + reversed_y
#
#
# print(reversed_y)
#
# z = "india"
#
# # using recursive function or recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
#
# reversed_z = reverse_string(z)
#
# print(reversed_z)
#
# # using stack
# a = "inadequate"
#
# def using_stack(s):
#     stack = []
#     for i in s:
#         stack.append(i)
#
#     s = ""
#     for _ in range(0, len(stack)):
#         s += stack.pop()
#
#     return s
#
#
# reversed_a = using_stack(a)
# print(reversed_a)
#
# # using reversed function
# b = "Propoganda"
# reversed_b = "".join(reversed(b))
# print(reversed_b)


################################ Palindrome ######################################3333

# x = input("enter you string")

# if x==reverse_string(x):
#     print("String is pallindrome")
# else:
#     print("string is not pallindorome")
#
# if x == x[::-1]:
#     print("String is pallindrome")
# else:
#     print("string is not pallindorome")


################################################ anagarm ##############################################

s1 = "wasp"
s2 = "swip"

# if sorted(s1) == sorted(s2):
#     print("they are anagram to each other")
# else:
#     print("they are not anagram to each other")

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in s1:
            if i not in s2:
                break
        else:
            return True
    return False

if check_anagram(s1,s2):
    print("they are anagram to each other")
else:
    print("they are not anagram to each other")


# count no of vowels & consonants

# x = input()
#
# vow_count = 0
# con_count = 0
#
# for i in x:
#     if i.lower() in "aeiou":
#         vow_count +=1
#     else:
#         con_count +=1
#
# print(f"No of vowels in string are{vow_count}")
# print(f"No of consonants in string are{con_count}")

# # given string is digit or not
#
# x = input()
#
# y = x.replace(" ", "")
# print(y)
#
# if y.isdigit():
#     print("string is a digit string")
# else:
#     print("string is not  a digit string")
#
# # # display duplicate character
# #
# x = input()
# duplicate = []
# x = x.lower()
#
# for i in x:
#     if x.count(i) > 1:
#         if i not in duplicate:
#             duplicate.append(i)
#
# print(duplicate)

## rotation string

# pan    npa
# panpan


# rotation  ationrot
# rotationrotation

x = input("enter x")
y = input("enter y")

if y in x+x:
    print(f'{y} is a rotation string of {x}')
else:
    print(f'{y} is not a rotation string of {x}')


