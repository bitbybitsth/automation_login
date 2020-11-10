
#packing

def fun(*args, **kwargs):
    for item in args:
        print(item)

    for key,val in kwargs.items():
        print(f"{key}  ->> {val}")


# fun(4,5,6,7,8,9,2,3,4,5,6,7,7, a=10, b=20, c=30)
#
#
# a = 1,2,3,7,8,9,2,4,5,6
#
# print(a)
# print(type(a))
#_____________________________________________________________________________________________
# unpacking

a,b,c = (1,2,3)   # both sides must have same number or arguments, no of references=no of values to unpack, otherwise error.

print(a)
print(b)
print(c)
#_____________________________________________________________________________________________
def function(a,b,c,d):
    sum = a+b+c+d
    print(sum)


x = [5, 6, 7, 8]



function(*x)

def api_login_request(username=None, password=None, apikey=None):
    if username and password and apikey:
        print("Login succeeded")
    else:
        print("Credential missing")


params = {"username":"bitbybit","apikey":"fgrtsf566DGHY45433DGGT3324234FFF"}
api_login_request(**params)

def get_data(name, last, email, ph=None, add=None, bg=None):
    if ph and add and bg:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com", "solapur", "o+", "9766588937"
    if ph and bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+", "9766588937"
    if ph and add:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "9766588937"
    if add and bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "o+"
    if ph:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com","9766588937"
    if bg:
        return "pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+"
    if add:
        return "pankaj","gosavi","pankajgosavi1029@gmail.com","solapur"


    return "pankaj","gosavi","pankajgosavi1029@gmail.com"



params = {"name":"pankaj", "last":"Gosavi", "email":"pa@gmail.com", "bg":"o+", "add":"9766"}
print(get_data(**params))



