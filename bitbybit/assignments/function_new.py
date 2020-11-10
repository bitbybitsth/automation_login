#

# n = int(input("Enter no:"))
# even_or_odd(n)


# def function_name(a,b):
#    total = a+b
#    mul = a*b
#    if mul%5==0:
#        return total, mul
#    sub = a-b
#    x = [total,mul,sub]
#    return x




#
# total= function_name(12,3)
# # total, mul = function_name(12,3)
#
# print(f"total --> {total}")
# # print(f"mul --> {mul}")
# # print(f"sub --> {sub}")
#


# def outer():
#     print("Entered in outer")
#
#     def inner():
#         print("entered in innner")
#     print("Outer calling inner")
#     print("returning inner")
#     return inner
#
#
# inn = outer()
# print("calling innner")
# inn()


# Global , Local, Non-local

URL = "www.facebook.com"

def messages():
    # x = 20
    # URL = "www.facebook.com/messages"
    def chats():
        URL = "www"
        URL = URL+"/Imageupload"
        print(f"chat1 -> {URL}")

    def chats1():
        # nonlocal URL
        URL =" "
        URL = URL+"/imageupload"
        print(f"chat2 -> {URL}")
    chats()
    chats1()
    print(URL.capitalize())


messages()
print(f"Base url -->{URL}")




# print(y)