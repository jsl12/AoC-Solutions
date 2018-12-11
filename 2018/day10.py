import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize(pos_df, n, type='single', fig=None, ax=None, close=True):
    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(19.2, 10.8))
    if type == 'single':
        ax.plot(pos_df['x'][n], pos_df['y'][n], '.')
    elif type == 'moving':
        for i, row in pos_df.iterrows():
            ax.plot(row['x'][:n], row['y'][:n], 'b')
    fig.savefig('day10.png')
    if close:
        plt.close(fig)
    else:
        return fig, ax

def make_dfs(input, n):
    REGEX = re.compile('position=< ?([-\d]+), +([-\d]+)> velocity=< ?([-\d]+), +([-\d]+)>')
    lines = input.splitlines()
    length = len(lines)
    x = np.empty(length, dtype=np.int32)
    y = np.empty(length, dtype=np.int32)
    x_vel = np.empty(length, dtype=np.int32)
    y_vel = np.empty(length, dtype=np.int32)

    def parse(line):
        match = REGEX.match(line)
        return {
            'pos': {'x': int(match.group(1)), 'y': int(match.group(2))},
            'vel': {'x': int(match.group(3)), 'y': int(match.group(4))},
        }

    for i, line in enumerate(lines):
        point = parse(line)
        x[i] = point['pos']['x']
        y[i] = point['pos']['y']
        x_vel[i] = point['vel']['x']
        y_vel[i] = point['vel']['y']
    df = pd.DataFrame({
        'x': x,
        'y': y,
        'x_vel': x_vel,
        'y_vel': y_vel
    })
    # construct position over time df
    if isinstance(n, tuple):
        r = np.arange(n[0], n[1], dtype=np.int32)
    elif isinstance(n, int):
        r = np.arange(n, dtype=np.int32)
    idx = pd.MultiIndex.from_product([['x', 'y'], np.arange(r[0], r[0] + r.size)])
    pos_df = pd.DataFrame(columns=idx, index=np.arange(length))
    df = pd.DataFrame(data=np.empty((length, r.size), dtype=np.int32))
    df.columns = df.columns + r[0]
    for i, row in df.iterrows():
        df.loc[i] = r

    pos_df['x'] = df.multiply(x_vel, axis=0).add(x, axis=0)
    pos_df['y'] = df.multiply(y_vel, axis=0).add(y, axis=0)

    return pos_df

def part1(input):
    dfp = make_dfs(input, n=(8000, 10000))
    fig, ax = visualize(dfp, 9000, close=False)
    for i in range(10):
        fig, ax = visualize(dfp, 200*i, close=False, fig=fig, ax=ax)
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))