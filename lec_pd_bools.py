import pandas as pd


data = {
    'date': [
        '2012-02-16 07:42:00',
        '2020-09-23 08:58:55',
        '2020-09-23 09:01:26',
        '2020-09-23 09:11:01',
        '2020-09-23 11:15:12',
        '2020-11-18 11:07:44',
        '2020-12-09 15:34:34',
        ],
    'firm': [
        'JP Morgan',
        'Deutsche Bank',
        'Deutsche Bank',
        'Wunderlich',
        'Deutsche Bank',
        'Morgan Stanley',
        'JP Morgan',
        ],
    'action': [
        'main',
        'main',
        'main',
        'down',
        'up',
        'up',
        'main',
        ],
}

data['date'] = pd.to_datetime(data['date'])
df = pd.DataFrame(data=data).set_index('date')


cond = df.loc[:, 'action'] == 'up'
res = df.loc[cond]
print(res)


new_cond = cond.array
res = df.loc[new_cond]
print(res)

print(df.loc[:, [True, False]])


crit = (df.loc[:, 'action'] == 'up') | (df.loc[:, 'action'] == 'down')
print(df.loc[crit])


# print(df.loc[crit])
