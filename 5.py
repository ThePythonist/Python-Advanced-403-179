import jdatetime
import datetime

# now = str(datetime.date.today()).split("-")
#
# jalali_now = jdatetime.date.fromgregorian(
#     day=int(now[2]),
#     month=int(now[1]),
#     year=int(now[0])
# )
#
# print(jalali_now)

# -------------------------------------------------------------------------

christmas = jdatetime.date.fromgregorian(day=25, month=12, year=2024)
print(christmas)
