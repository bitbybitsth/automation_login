from datetime import date, time

today = date.today()
cdate = date(day=20, month=5, year=1990)

print(today)


print(date.weekday(today))
# 0 6
# monday sunday
#
# 1 - 7
# monday sunday
print(date.isoweekday(today))

print(date.max)
print(date.min)

print(today.replace(day=21))
today.strftime("%y-%m-%d")



# time

x = time(10,20,30)
print(x)
x.replace(hour=12)
print(x.max)
print(x.min)
x.strftime("%H:%M:%S")
