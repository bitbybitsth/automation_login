






def function_name(param1 = "pankaj", param2= "gosavi"):
    print(param1)
    print(param2)


function_name(param2="ms",param1="dhoni")

print("*************************************", function_name())

def display(param1, param2, *args, **kwargs):
    print(f"param1 -> {param1}")
    print("param2 ->", param2)

    for arg in args:
        print(arg)

    # print(f"param3 --> {param3}")

    for key, value in kwargs.items():
        print(f"{key} --> {value}")




# display("thursday", "friday", "saturday", "sunday", "tuesday", "monday", param3="funday", preday= "wednesday", repat="thursday")

# display("thursday", "friday", param3="sat")
#
# display("thursday", "friday", "saturday", "sunday", "tuesday", "monday", param3="funday")

def addition(num1, num2, num3, *args, num4):
    total = num1+num2+num3
    for num in args:
        total += num
    total +=num4
    return total

total = addition(10, 20,30,num4=70 )
print(total)

