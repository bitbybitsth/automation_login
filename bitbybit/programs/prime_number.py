

n = int(input("Enter Number:"))

if n>1:
    divisor = [x for x in range(2, (n//2)+1)]
    print(divisor)
    for div in divisor:
        print("*****")
        if n%div == 0:
            print(f"{n} is not prime")
            print(f"{div} times {n//div} is {n}")
            break
    else:
        print(f"{n} is prime")
else:
    print("number is not prime")


# x = [x for x in range(1, n+1)]
# print(x)
# fact = 1
#
# for multilper in x:
#     fact *= multilper
#
# print(fact)

