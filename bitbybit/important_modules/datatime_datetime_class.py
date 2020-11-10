import datetime as dt


datetime_now = dt.datetime.now()
print("datetime now", datetime_now)

print(datetime_now.year)
print(datetime_now.month)
print(datetime_now.day)
print(datetime_now.hour)

datetime_utc = dt.datetime.utcnow()
print("UTC Datetime", datetime_utc)

# creating datetime

dt_time = dt.datetime(2020, 12,10,3,45,45,999999)
print("Created Time:",dt_time)





# posix/epoch time
dt_timestamp = datetime_now.timestamp()
print("Time stamp", dt_timestamp)

date_from_timestamp = dt.datetime.fromtimestamp(dt_timestamp)
print("date_from_timestamp", date_from_timestamp)

current_date = datetime_now.date()

current_time = datetime_now.time()

print("Current Date", current_date)
print("Current Time", current_time)

combined_time = dt.datetime.combine(current_date, current_time)
print("Combined time:", combined_time)

replaced_datetime =dt_time.replace(year=2021, hour=10, minute=10, month=1, day=23)
print("replaced_datetime", replaced_datetime)

x = "2021-13-06 02:15:23"


# https://www.programiz.com/python-programming/datetime/strptime    
date_from_string = dt.datetime.strptime(x, "%Y-%d-%m %H:%M:%S")
print("date_from_string", date_from_string)
print(type(date_from_string))

date_to_string = dt_time.strftime("%Y-%d-%m %H:%M:%S")
print("String date:", date_to_string)
print(type(date_to_string))


x = "2020-07-27 7:05:59"
cdate = dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
print(cdate)
print(type(cdate))