"""the time module is principally for working with unix time stamps; expressed
as a floating point number taken to be seconds since the unix epoch. the
datetime module can support many of the same operations, but provides a more
object oriented set of types, and also has some limited support for time zones."""

import time

# no second arg, local time will be given
CUR_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")
print(CUR_TIME)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
# Locale’s appropriate date and time representation.
print(time.strftime("%c"))

# timestamp
print("time.time(): %f " % time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

# use time package is usually enough!
from datetime import datetime
print(datetime.now().time())
print("datetime: " + str(datetime.now()))
print("datetime: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
