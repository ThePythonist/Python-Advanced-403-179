from persiantools.jdatetime import JalaliDateTime
import pytz

x = JalaliDateTime(1403, 4, 30, 18, 28, 0, 0, pytz.utc).strftime("%A")
print(x)
