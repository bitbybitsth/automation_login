
def even_or_odd(number):
    if number%2 ==0:
        return True
    else:
        return False

def function_name(x):
    if x==10:
        print(10)


# list out even number from give list



# l = [45,65,68,89,98,34,56,12,34,56,87,46,64]
#
# # for i in l:
# #     if even_or_odd(i):
# #         print(f"{i} is even")
# #
# # for i in l:
# #     if not even_or_odd(i):
# #         print(f"{i} is odd")
#
# even = [i for i in l if i%2==0]
# odd = [i for i in l if i%2!=0]
# print(even)
# print(odd)

# --------------------------------------------------------------
# fibonaci series

def fibonacci(number):
    """
    Fibonacci sesries
    0 1 1 2 3 5 8 13 21 34 55
    any number in the series is addition of earlier two numbers.
    start with 0 1 as starting number

    :param l: number of fibonaci series elements
    :return:
    """
    # first = 0
    # second = 1
    # print(first , second)
    # for _ in range(0, number-2):
    #     third = first + second
    #     print(third)
    #     first = second
    #     second = third
    fib_list = [0, 1]
    for i in range(0,number-2):
        fib_list.append(fib_list[i] + fib_list[i+1])
    return fib_list


# fib_list = fibonacci(10)
# even_or_odd(5)
# print(fib_list)

# ---------------------------------------------

# factorial

def factorial(n):
    """
    1*2*3*4*5*6*....*n
    :param n:
    :return:
    """
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n*recursive_fact(n-1)


# fact = recursive_fact(5)
# print(fact)

# ---------------------------------------
# Prime number
#
# def is_prime(n):
#     if n == 0:
#         return False
#     for i in range(2, n//2):
#         if n%i==0:
#             return False
#     return True
#
# x = is_prime(21)
# if x:
#     print("Number is Prime")
# else:
#     print("Number is not prime")

# -----------------------------------------------
# hacker rank - FizzBuzz
# number%3 == 0 print(Fizz)
# number%5 == 0 print(Buzz)
# number%15 == 0 print(FizzBuzz)
# print(number)

def f(n):
    print("FizzBuzz") if n%15==0 else print("Buzz") if n%5==0 else print("Fizz") if n%3==0 else print(n)
    # if n%15==0:
    #     print("FizzBuzz")
    # elif n%5 == 0:
    #     print("Buzz")
    # elif n%3 == 0:
    #     print("Fizz")
    # else:
    #     print(n)



f(19)





