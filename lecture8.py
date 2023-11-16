"""Creating a datetime object for the current time:"""
import datetime as dt

dt_now = dt.datetime.now()
print(dt_now)

"""Printing datetime and string representations:"""
import datetime as dt
dt_now = dt.datetime.now()
str_now = '2023-10-31 11:12:15.377855'

print(dt_now)

"""Using the repr function on a datetime object:"""
print(repr(dt_now))

"""Creating a specific datetime object:"""
import datetime as datetime
new_obj = datetime.datetime(
    year=2022,
    month=11,
    day=1,
    hour=8,
    minute=0,
    second=0,
    microsecond=0)

utils.pp_cfg.sep = True
utils.pp_cfg.show_type = True

dt0 = dt.datetime(
    year=2022,
    month=11,
    day=1,
    hour=8,
    minute=0,
    second=0,
    microsecond=0)

start = dt.datetime(year=2020, month=12, day=31, hour=0)
end = dt.datetime(year=2020, month=12, day=31, hour=12)

new_delta =  end - start


bday = dt.datetime(1974, 11, 8, hour=8, minute=45)
dt_now = dt.datetime.now()
alive = dt_now - bday

secs = (alive.days * 24 * 60 * 60) + alive.seconds

res = f"I have been alive for {secs:,.0f} secs"

days = 1340
future = dt.datetime.now() + dt.timedelta(days=days)

alive = future - bday

age = alive.days/365.
res = f"In {days} days, I'll be {age:.2f} years"


import os
import datetime as dt

import pandas as pd

from webinars import lec_utils as utils
import toolkit_config as cfg



utils.pp_cfg.sep = True
utils.pp_cfg.df_info = True
utils.pp_cfg.df_max_rows = 100
utils.pp_cfg.df_max_cols = 10

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = True
utils.pp_cfg.df_max_rows = 100
utils.pp_cfg.df_max_cols = 10

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')