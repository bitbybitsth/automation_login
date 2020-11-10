
# f_ob = open("team_india.txt", "r")
# #
# # file_contents = f_ob.read()
# # print(file_contents)
# # f_ob.write("Pankaj")
# #
# first_line = f_ob.readline()
# second_line = f_ob.readline()
# third_line = f_ob.readline()
# #
# # print(first_line, end="")
# # print(second_line,end="")
# # print(third_line,end="")
# #
# file_lines = f_ob.readlines()
# print(file_lines)
#
#
# f_ob.close()

# #
# with open("team_india.txt") as f_ob:
#     first_line = f_ob.readline()
#     second_line = f_ob.readline()
#     # third_line = f_ob.readline()
#     #
#     print(first_line, end="")
#     print(second_line, end="")
#     # print(third_line, end="")
#     #
#     file_lines = f_ob.readlines()
#     print(file_lines)


    #
    # fc = f_ob.read()
    # if "Virat" in fc:
    #     print("True")

# with open("team_india.txt", 'r') as rf:
#     with open("sample1.txt", 'a') as wf:
#         fc = rf.read()
#         wf.writelines(fc)


import os
# if os.path.isfile("C:\\Users\\hp\\Desktop\\3b.jpg"):
with open("C:\\Users\\hp\\Desktop\\3bb.jpg",'rb') as rrb:
    with open("bbb.jpg", 'wb') as wwb:
        fc = rrb.read()
        wwb.write(fc)



# print(f_ob.read())
