def pattern1(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    :param n: n is input for no of lines
    :return: None
    """
    for i in range(1, n+1):  # use for new line [1 ,2 ,3 ,4]
        # print("* "*i)
        for j in range(1, i+1):  # for printing stars
            print(f"{j}", end=" ")
        print("")


x = int(input("enter n:"))

# pattern1(x)

def pattern2(n):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(n,-1,-1):
        print("* "*i)
        # for j in range(0, i):
        #     print("*", end=" ")
        # print("")

# pattern2(x)

def patter3(n): # most important
    """
         *
        * *
       * * *
      * * * *
     * * * * *
    """
    for i in range(0,n):
        print(" "*n+"* "*(i+1))
        n-=1
        # for j in range(0, n):
        #     print(end=" ")
        # n -=1
        # for j in range(0,i+1):
        #     print("*", end=" ")
        # print("")


# patter3(x)

def patter4(n): # most important
    """
    * * * * *
     * * * *
      * * *
       * *
        *
    """
    for i in range(n,-1, -1):
        # print(" "*n+"* "*(i+1))
        # n-=1
        for j in range(0, n):
            print(end=" ")
        n +=1
        for j in range(0,i+1):
            print("*", end=" ")
        print("")

pattern1(7)
# pattern2(5)
#
# patter3(5)
# patter4(5)



