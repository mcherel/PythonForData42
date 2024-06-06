#!/usr/bin/env python3.10

#allowed time datetime and all date libraries

import datetime as dt
import time as t

time_stamp = t.time()
print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")

current_time = dt.datetime.now()

#printing current date in "Mon day year" format
print(current_time.strftime("%b %d %Y"))