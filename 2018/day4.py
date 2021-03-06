import re
import pandas as pd
from datetime import datetime, timedelta

DATE_REGEX = re.compile('\[\d+-(\d+-\d+ \d+:\d+)\]')
BEGIN_REGEX = re.compile('.+Guard #(\d+)')
EVENT_REGEX = re.compile('.*(begins shift|falls asleep|wakes up)')

def part1(input):
    df = event_df(input)
    dft = time_df(df)
    df = count_df(dft)

    guard = df[df['Count'] == df['Count'].max()].index[0]
    min_totals = dft[dft['Guard'] == guard].select_dtypes('bool').sum()
    min = min_totals[min_totals == min_totals.max()].index[0]
    return guard * min

def part2(input):
    df = event_df(input)
    dft = time_df(df)
    guard, min = max_minute(dft)
    return guard * min

def max_minute(df):
    res = [(g[0], g[1].select_dtypes('bool').sum()) for g in df.groupby('Guard')]
    res2 = [(g[0], g[1].loc[g[1].iloc[:].idxmax()], g[1].idxmax()) for g in res]
    df = pd.DataFrame({
        'Guard': [g[0] for g in res2],
        'Minutes Asleep': [g[1] for g in res2],
        'Max Minute': [g[2] for g in res2]
    }).set_index('Guard')

    most_asleep_guard = df['Minutes Asleep'].idxmax()
    sleepiest_minute = df.loc[most_asleep_guard]['Max Minute']
    return most_asleep_guard, sleepiest_minute

def event_df(input):
    df = pd.DataFrame([proc_line(line) for line in input.splitlines()])
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df

def time_df(event_df):
    event_df.index = [correct_begin(idx) for idx in event_df.index]
    res = []
    for day in event_df.groupby(pd.Grouper(freq='D')):
        res.append({
            'Date': day[0],
            'Guard': int(find_guard(day)),
        })
        for i in range(60):
            res[-1][i] = False

        df = day[1]
        # For each falling asleep event
        for date, event in df[df['Event'] == 'falls asleep'].iterrows():
            # Find the next wakeup time
            wakeup = df[df.index > date].iloc[0]
            for i in range(date.minute, wakeup.name.minute):
                res[-1][i] = True

        # print(day[0])
        # print(find_guard(day))
    df = pd.DataFrame(res)
    df = df.set_index('Date')
    return df

def count_df(time_df):
    guards = []
    counts = []
    for g in time_df.groupby('Guard'):
        guards.append(g[0])
        counts.append(g[1].select_dtypes('bool').sum(axis=1).sum())
    df = pd.DataFrame({'Guard': guards, 'Count': counts})
    df = df.set_index('Guard')
    return df

def correct_begin(index):
    if index.hour == 23:
        return index.replace(minute=0) + timedelta(hours=1)
    else:
        return index

def find_guard(day):
    df = day[1]
    found = df[df['Event'] == 'begins shift']['Guard']
    assert len(found) == 1
    return found[0]

def proc_line(line):
    try:
        g = int(BEGIN_REGEX.match(line).group(1))
    except AttributeError:
        g = None
    res = {
        'Date': datetime.strptime(DATE_REGEX.match(line).group(1), '%m-%d %H:%M'),
        'Guard': g,
        'Event': EVENT_REGEX.match(line).group(1)
    }
    return res

if __name__ == '__main__':
    import input as inp
    DAY = 4
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))
