import re
import pandas as pd
from datetime import datetime, timedelta

DATE_REGEX = re.compile('\[\d+-(\d+-\d+ \d+:\d+)\]')
BEGIN_REGEX = re.compile('.+Guard #(\d+)')
EVENT_REGEX = re.compile('.*(begins shift|falls asleep|wakes up)')

def part1(input):
    df = event_df(input)
    df = time_df(df)
    return

def event_df(input):
    df = pd.DataFrame([proc_line(line) for line in input.splitlines()])
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df

def time_df(event_df):
    event_df.index = [correct_begin(idx) for idx in event_df.index]

    for day in event_df.groupby(pd.Grouper(freq='D')):
        print(day)
    return event_df

def correct_begin(index):
    if index.hour == 23:
        return index.replace(minute=0) + timedelta(hours=1)
    else:
        return index

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

def part2(input):
    return

if __name__ == '__main__':
    from pathlib import Path
    p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark\AoC-Inputs\2018')
    with open(p / 'day4.txt', 'r') as file:
        input = file.read()
    print(part1(input))
    # print(part2(input))