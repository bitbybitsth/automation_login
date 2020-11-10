# def function():
#     yield 1
#     yield 2
#     yield 3
#
#
# x = function()
# print(x)
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# x = [x for x in range(1000000)]
# print(x)

def function():
    for i in range(1000000):
        yield i

x = function()

n = 0
while n<100:
    print(next(x))
    n+=1

n = 0
while n<100:
    print(next(x))
    n+=1

#
# def fiboancci_gene(n):
#     # numbner 0 1 2 3 5, 8, 13
#     a, b = 0, 1
#     i=0
#     while i<n:
#         yield a
#         a, b = b, a+b
#         i+=1
# #
# # fib = list(fiboancci_gene(10))
# # print("1st time using generator")
# #
# # for fi in fib:
# #     print(fi)
# #
# # for fi in fib:
# #     print(fi)
#
# #
# # def fibo_list(n):
# #     l = [0,1]
# #     for i in range(0, n-2):
# #         l.append(l[i]+l[i+1])
# #     return l
# #
# # fibList = fibo_list(10)
# # print("1st time using list")
# # for fi in fibList:
# #     print(fi)
# #
# # print("need fibonaci numbers one more time")
# # for fi in fib:
# #     print(fi)
# #
# #
# # print("need fibonaci numbers one more time")
# # for fi in fibList:
# #     print(fi)
#
# x = [x for x in range(1, 10)]
#
# y = (x*x for x in range(1, 10))
#
# print(x)
# print(y)
# for i in y:
#     print(i)
#
# def function(y):
#     print(next(y))
#     print(next(y))
#     print("***********")
#     for i in y:
#         print(i)
#
# # print("**********88")
# # function(x*x for x in range(1, 10))
# #
# # def fun(x):
# #     yield from fiboancci_gene(x)
# #
# # g = fun(10)
#
#
# # print(g)
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# """
# Generators:
# any function containing a yield statement is a generator function.
# generator function yields value one by one
# generator will give us the next value when we request
# generator function remember the last state(value) returned and continues execution after that.
# generator function can be exhaust only once
# after the generator is exhausted and if we request for next value it will raise StopIteration error
# generator can be defined/crated using generator expression
# eg: (x+x for x in range(10))
# we can reset the generator by converting it to list.
# """
