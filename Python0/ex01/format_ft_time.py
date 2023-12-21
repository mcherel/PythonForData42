#!/usr/bin/env python3.10
# to execute:
# chmod +x format_ft_time.py
# ./format_ft_time.py

#allowed time datetime and all date libraries

from datetime import datetime
import time

time_stamp = time.time()
print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")

current_time = datetime.now()

#printing current date in "Mon day year" format
print(current_time.strftime("%b %d %Y"))