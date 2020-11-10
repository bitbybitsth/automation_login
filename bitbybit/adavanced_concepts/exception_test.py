#
# try:
#     try:
#         print("printing from innner try", x[3])
#     except IndexError:
#         print(x[5])
#     else:
#         pass
#     finally:
#         pass
# except (IndexError, Exception):
#     print("outer except block caught the exception")

x = [1, 2, 34]
d = {"event": "bhumi pujan", "date":"5th aug"}
def simple_geerator():
    yield 1
    yield 2


try:
    print(x[2])
    print(d.get("status"))
    raise Exception
    f = simple_geerator()
    print(next(f))
except Exception:
    print("Except blocks line 1")
    print("Except blocks line 2")
else:
    print("else blocks line1")
    print("else blocks line2")
finally:
    print("Finally blocks line1")
    print("Finally blocks line2")