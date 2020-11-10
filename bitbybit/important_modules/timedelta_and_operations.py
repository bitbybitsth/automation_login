import datetime


d = datetime.timedelta(minutes=15)
d2 = datetime.timedelta(minutes=5)

print(d)
print(d.total_seconds())



now = datetime.datetime.now()
cdate = datetime.datetime(2020,7,23)




diff = now - cdate
print(diff)
print(type(diff))

diff = now+cdate


print(now>cdate)
print(now == cdate)


