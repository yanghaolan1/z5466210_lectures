lst = [1, 2, 3]
lst[0]

lst = [1, 2]
print( id(lst) )

lst0 = [1, 2]
lst1 = [1, 2]
lst2 = lst0

lst2[0] = -99

dic = {'a': 1, 2: 3}
dic['a']
dic[2]

lst = [1, 2, 3]
lst[0]


#pd.read_csv('file_path.csv')

#df.to_csv('file_path.csv')


import copy
import pprint as pp

def printit(obj, msg):
    sep = '-' * 30
    to_print = [
        sep,
        msg,
        '',
        pp.pformat(obj),
        '',
        f"Type: {type(obj)}",
        f"Object Address: {id(obj)}",
        sep,
    ]
    print('\n'.join(to_print))

def example1():
    lst0 = [1, 2]
    printit(lst0, "EXAMPLE 1: This is lst0")
    lst1 = [1, 2]
    printit(lst1, "EXAMPLE 1: This is lst1")

def example2():
    lst0 = [1, 2]
    lst1 = [1, 2]
    lst2 = lst0
    printit(lst0, "EXAMPLE 2: This is lst0")
    printit(lst1, "EXAMPLE 2: This is lst1")
    printit(lst2, "EXAMPLE 2: This is lst2")

def example3():
    lst0 = [1, 2]
    lst1 = [1, 2]
    lst2 = lst0
    printit(lst0, "EXAMPLE 3: This is the ORIGINAL lst0")
    printit(lst1, "EXAMPLE 3: This is the ORIGINAL lst1")
    printit(lst2, "EXAMPLE 3: This is the ORIGINAL lst2")
    lst2[0] = -99
    printit(lst0, "EXAMPLE 3: This is lst0 after setting lst2[0] = -99")
    printit(lst1, "EXAMPLE 3: This is lst1 after setting lst2[0] = -99")
    printit(lst2, "EXAMPLE 3: This is lst2 after setting lst2[0] = -99")

def example4():
    lst0 = [1, 2]
    lst1 = [3, [1, 2]]
    printit(lst0, "EXAMPLE 4: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 4: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 4: This is lst1[1] (the inner list)")

def example5():
    lst0 = [1, 2]
    lst1 = [3, [1, 2]]
    lst2 = [3, lst0]
    printit(lst0, "EXAMPLE 5: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 5: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 5: This is lst1[1] (the inner list)")
    printit(lst2, "EXAMPLE 5: This is lst2 (the outer list)")
    printit(lst2[1], "EXAMPLE 5: This is lst2[1] (the same list as lst0)")

def example6():
    lst0 = [1, 2]
    lst1 = copy.copy(lst0)
    printit(lst0, "EXAMPLE 6: This is lst0")
    printit(lst1, "EXAMPLE 6: This is lst1")

def example7():
    lst0 = [1, 2]
    lst1 = [3, lst0]
    lst2 = copy.copy(lst1)
    printit(lst0, "EXAMPLE 7: This is lst0")
    printit(lst1, "EXAMPLE 7: This is lst1")
    printit(lst2, "EXAMPLE 7: This is lst2")
    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst1[1], "EXAMPLE 7: This is lst1[1]")
    printit(lst2[1], "EXAMPLE 7: This is lst2[1]")
    lst3 = copy.deepcopy(lst1)
    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst3[1], "EXAMPLE 7: This is lst3[1] (different than lst0)")

def main():

    if __name__ == "__main__":
        main()


import pprint as pp
import pandas as pd

def printit(obj, msg=None):
    sep = '-'*40
    if isinstance(obj, str) and obj == '?':
        return None
    elif isinstance(obj, str):
        prt = obj
    elif isinstance(obj, (pd.DataFrame, pd.Series)):
        prt = obj.to_string()
    else:
        prt = pp.pformat(obj)
    if not isinstance(obj, str):
        prt = f'{prt}\n\nType: {type(obj)}'
    if msg is not None:
        prt = f'{msg}\n\n{prt}'
    to_print = [
        '',
        sep,
        prt,
        sep,
    ]
    print('\n'.join(to_print))

dates = [
    '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15',
]
prices = [
    7.1600, 7.1900, 7.0000, 7.1000, 6.8600, 6.9500, 7.0000, 7.0200, 7.1100, 7.0400,
]
bday = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

ser = pd.Series(data=prices, index=dates)
df = pd.DataFrame(data={'close': ser, 'bday': bday}, index=dates)

label = '2020-01-10'
res  = '?'

label = '2020-01-30'

label_seq = ['2020-01-10', '2020-01-13']
res  = '?'

label_seq = ['2020-01-10', '2020-01-11']

start = '2020-01-10'
end = '2020-01-13'
res  = '?'

start = '3020-01-10'
end = '2020-01-13'
res  = '?'

start = 'start'
end = 'end'
res  = '?'

ser2 = ser.copy()

old_label = '2020-01-10'
new_label = '2020-01-11'

start = '2020-01-10'
end = '2020-01-13'

new_label = '2020-01-11'


label = '2020-01-02'


rlabel = '2020-01-02'
clabel = 'close'


rlabel_seq = ['2020-01-02', '2020-01-06']
clabel = 'close'


rlabel_seq = ['2020-01-02', '2020-01-06']
clabel = 'close'

rlabel = '2020-01-02'
rlabel_seq = ['2020-01-02', '2020-01-06']
clabel = 'close'
clabel_seq = ['close', 'bday']


clabel_seq = ['bday', 'close']


rstart = '2020-01-10'
rend = '2020-01-15'

import os
import pprint as pp

import pandas as pd

import toolkit_config as cfg

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_NOHEAD_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_header.csv')
QAN_NOINDEX_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_index.csv')


def print_df(df):

    if isinstance(df, str) and df == '?':
        return
    elif not isinstance(df, pd.DataFrame):
        raise Exception("Parameter `df` must be a data frame")
    sep = '-' * 40
    to_print = [
        '',
        sep,
        pp.pformat(df),
        '',
    ]
    print('\n'.join(to_print))
    df.info()
    print('\n'.join(['', sep]))