import datetime

# x = "2020-07-23 09:51:12"
#
# # error_messge = {"error_message": "Please enter a valid username or email address"}
# #
# # def function():
# #     return error_messge
# #
# # def function1():
# #     return error_messge
#
#
#
# format = "%d-%m-%Y %H:%M:%S"
# y = "sun 21 may, 2017"
#
# cr_dt = datetime.datetime.now()
# print(cr_dt)
#
#
# dt = datetime.datetime.strptime(x, "%d-%m-%Y %H:%M:%S")
# print(dt)
#
# dt_string = dt.strftime(format)
# print(dt_string)
#
# dt = dt.strptime(cr_dt.strftime(format), format)
# print(dt)
# print(type(dt))


def format_date(dt):
    """
    20 June 2018 2:30:30 PM
    2020-07-21
    14:30:30
    :param dt:
    :return:
    """
    dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    f_date = dt.date()
    f_time = dt.time()
    date_string = f_date.strftime('%d %B %Y')
    hour = f_time.hour
    suffix = " PM UTC" if hour>11 else " AM UTC"
    hour = hour if hour<12 else (hour+11)%12 +1
    f_time = f_time.replace(hour=hour)

    return date_string + " " + str(f_time) +suffix


dates = format_date("2020-07-21 14:30:30")
print(dates)








# dt = dt.strptime("")

