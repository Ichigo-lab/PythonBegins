from datetime import datetime, timedelta
import time
# Timestamp
# print(time.time())


# def send_emails():
#     for i in range(100000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)


dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)

duration = dt2 - dt1
print(duration)
print("Days", duration.days)
print("seconds", duration.seconds)
print("tseconds", duration.total_seconds())
