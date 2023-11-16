import pandas as pd
from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False

def mk_rec_df0(show: bool = False):
    cnts_rec_csv = '''
    date                , firm           , action
    2012-02-16 07:42:00 , JP Morgan      , main
    2020-09-23 08:58:55 , Deutsche Bank  , main
    2020-09-23 09:01:26 , Deutsche Bank  , main
    2020-09-23 09:11:01 , Wunderlich     , down
    2020-09-23 11:15:12 , Deutsche bank  , up
    2020-11-18 11:07:44 , Morgan Stanley , up
    2020-12-09 15:34:34 , JP Morgan      , main
    '''
    df = utils.csv_to_df(cnts_rec_csv, index_col='date', parse_dates=['date'])
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')
    if show is True:
        utils.pprint(df, "Example DF:")
    return df

def groupby_example0():
    df = mk_rec_df0(show=True)
    groups  = df.groupby('firm')
    obj = groups.groups

def groupby_example1():
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    groups = df.groupby(['firm', 'event_date'])

def mk_rec_df1():
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    groups = df.groupby(['event_date', 'firm'])
    df = groups.last().reset_index()
    return df

def bool_example0():
    df = mk_rec_df1()
    cond = df.loc[:, 'action'] == 'up'
    res = df.loc[cond]

def mk_event_df0():
    df = mk_rec_df1()
    crit = df.loc[:, 'action'].str.contains('up|down')
    df = df.loc[crit]
    event_df = df.copy()
    event_df.loc[:, 'event_type'] = event_df.loc[:, 'action'].apply(_et)
    cols = ['firm', 'event_date', 'event_type']
    event_df = event_df.loc[:, cols]
    event_df.reset_index(inplace=True, drop=True)
    event_df.index = event_df.index + 1
    event_df.index.name = 'event_id'
    return event_df

def apply_example0():
    df = mk_event_df0()
    df.loc[:, 'event_type'] = df.event_type.str.upper()
    res = df.apply(max)
    res = df.apply(max, axis=1)
    res = df.apply(sel_lower, pos=0)

if __name__ == "__main__":
    pass

import textwrap
import pandas as pd
from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False

def _join_msg(msg):
    return textwrap.dedent(msg)

def example_joins():
    left_cnts = '''
        idx , L  
        1   , L1 
        2   , L2 
        3   , L3 
        '''
    left = utils.csv_to_df(left_cnts, index_col='idx')

    right_cnts = '''
        idx , R  
        3   , R3 
        4   , R4 
        5   , R5 
        '''
    right = utils.csv_to_df(right_cnts, index_col='idx')

    res = left.join(right, how='left')
    res = left.join(right, how='right')
    res = left.join(right, how='inner')
    res = left.join(right, how='outer')

def example_df_plus_obj():
    cnts = '''
        idx , L  , R  
        1   , 11 , 12 
        2   , 21 , 22 
        3   , 31 , 32 
        '''
    base = utils.csv_to_df(cnts, index_col='idx')

    cnts = '''
        idx , R  
        3   , 3 
        4   , 4 
        5   , 5 
        '''
    other_df = utils.csv_to_df(cnts, index_col='idx')

    res = base + other_df
    res = base + other_df.loc[:, 'R']

def example_ret_and_mkts():
    cnts_mkt_csv = '''
        date       , mkt
        2020-09-18 , -0.0088
        2020-09-21 , -0.0108
        2020-09-22 , 0.0102
        2020-09-23 , -0.0248
        2020-09-24 , 0.0025
        2020-09-25 , 0.0172
        '''
    df_mkt = utils.csv_to_df(cnts_mkt_csv, index_col='date', parse_dates=['date'])

    cnts_ret_csv = '''
        date       ,   ret
        2020-09-21 , 0.016375
        2020-09-22 ,-0.055987
        2020-09-23 ,-0.103411
        2020-09-24 , 0.019534
        2020-09-25 , 0.050414
        '''
    df_ret = utils.csv_to_df(cnts_ret_csv, index_col='date', parse_dates=['date'])

    combined = df_ret.join(df_mkt, how='inner')

if __name__ == "__main__":
    pass