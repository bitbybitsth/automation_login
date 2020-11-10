from function_new import even_or_odd

# def function_name(arguments, agruments2, arguments3):
#     pass





n = int(input("Enter Number:"))

even_or_odd(n)


def fibonacci_series(n: int, fib_list: list) -> list:
    i = 0
    j = 1
    while n>0:
        fib_list.append(fib_list[i] + fib_list[j])
        i +=1
        j +=1
        n -=1
    return fib_list
#
# #
# # fib_list = fibonacci_series(fib_list=[0,1], n=n)
# #
# # fib_list2 = fibonacci_series(20, [0,1])
# # print(fib_list)
# # print(fib_list2)
# # fib_list_legth_20 = fibonacci_series(20,[0,1])
# # print(fib_list_legth_20)
#
#
#
# def function_name(a:int, b: int, c: list, s=15):
#     print(f"a={a}")
#     print(f"b={b}")
#     print(f"c={c}")
#     print(f"s={s}")
#     # for item in args:
#     #     print(item)
#     #
#     # for key,val in kwargs.items():
#     #     print(f"{key} --> {val}")
#
#
# sum = function_name(a=1,b=2, c=10)
# print(sum)