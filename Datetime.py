# import datetime

# now = str(datetime.datetime.now())
#
# print(now.split())
# print(now.split()[0])

# ---------------------------------------

# import time
#
# m = 60
# time.sleep(2 * m)
# now2 = str(datetime.datetime.now())

# ---------------------------------------

# import datetime
#
# year = datetime.datetime.now().year
# month = datetime.datetime.now().month
# minute = datetime.datetime.now().minute
# day = datetime.datetime.now().day
# hour = datetime.datetime.now().hour
# second = datetime.datetime.now().second
#
# print(f"{hour}:{minute}")

# ---------------- STRFTIME EXAMPLES ----------------

import datetime

now = datetime.datetime.now()
print(now.strftime("%m"))
