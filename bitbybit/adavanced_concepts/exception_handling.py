#_____________________________________________________________________________________________

# #################Syntax Errors
# print("Happy Rakshabandhan:")
# for in range(10):
#     if i>20

#_____________________________________________________________________________________________

d = {"event":"bhumi pujan", "date":"5th aug"}
## Runtime errors - Exception.
#
# x = int(input("Enter first number"))
# y = int(input("enter second number"))

### EXception handling example

# try:
#     result = x/y   # this can raise an exception
#     print(result)  # this will not execute if exception is raised
#     print("******8") # # this will not execute if exception is raised
#     print("$$$$$$$$$$$$$$$") # this will not execute if exception is raised
# except ZeroDivisionError:
#     print("Second number cannot be zero")

#_____________________________________________________________________________________________
# Multiple Except

def simple_geerator():
    yield 1
    yield 2

def function():
    with open("decorators.py") as f:
        pass
    # print(d["chief_guest"])
    x = simple_geerator()
    print(next(x))
    print(next(x))
    # print(next(x))
    # print(10+"good")
    return f

# try:
#     # function()
#     pass
# except FileNotFoundError:
#     print("****")
# except KeyError:
#     d.update({"chief_guest":"namo"})
#     print(d)
# except StopIteration:
#     print("Sorry our generator yield only 2 values, generator exhausted")
# except Exception as e:
#     print("Sorry our program got some exception, will update you with details")

#_______________________________________________________________________________________________
# default except

# try:
#     function()
# except:
#     print("Exception occurred and handled but doesn't have any details to display")




#_______________________________________________________________________________________________

# Try Except Finally

# try:
#     f = open("records.txt")
#     print(f.read())
#     next(f)
# except StopIteration:
#     print("Stop")
# finally:
#     f.close()



# print(f.closed)

# f = open("records.txt", "a")
# f.write("second record")

#_______________________________________________________________________________________________
# def fun():
#     login()
#
#     try:
#         params = {"date": "4:8:2020"}
#         result = request.get("facebook.com", params=params)
#     except (FileNotFoundError, KeyError, StopIteration, Exception) as e:
#         login()
#     else:
#         display_posts_on_wall()
#     finally:
#         # logout()






    # print(f.read())


print(fun())
# try except
# try except else
# try except finally
# try except else finally

















