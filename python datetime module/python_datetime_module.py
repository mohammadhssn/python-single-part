import datetime as dt


# time

# t = dt.time(12, 20, 3)
# print(t)
# print(t.hour)


# ---------------------------------------------------------------------------------------------------------------------

# # date
#
# d = dt.date(2000, 12, 23)
# print(d)
# print(d.day)

# d1 = dt.date.today()    # zaman alan
# print(d1)

# print(dt.date.fromtimestamp(122345))# yek meghdar bar hasbe second migire va zamani ke az epoch gozashte ro neshoon mide

# d1 = dt.date(2000, 4, 4)
# d2 = dt.date(2019, 1, 20)
# print(d2 - d1)

# ---------------------------------------------------------------------------------------------------------------------

# # datetime
#
# d = dt.datetime(1999, 2, 21, hour=3, minute=23, second=12)
# print(d)
# print(d.hour)
#
# d1 = dt.datetime.now()   # zaman alan
# print(d1)


# ---------------------------------------------------------------------------------------------------------------------

# # timedelta

# date = dt.date(1980, 2, 12)
#
# timedelta = dt.timedelta(weeks=3, days=2, hours=12, minutes=12, seconds=23)
#
# print(date - timedelta) # tirikhi ke dadim ro az timedelta kam mikone
# print(date + timedelta) # tirikhi ke dadim ro ba timedelta jame mikone


# ---------------------------------------------------------------------------------------------------------------------

# # pytz (timezone)
#
# import pytz
#
# local = dt.datetime.now()
#
# new_york = dt.datetime.now(pytz.timezone("America/New_York"))
#
# print(local)
# print(new_york)
#
# for i in pytz.all_timezones:
#     print(i)