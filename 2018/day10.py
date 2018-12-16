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
            x_data = row['x'][:n]
            y_data = row['y'][:n]
            ax.plot(x_data, y_data, 'b')
            ax.plot(x_data.iloc[-1], y_data.iloc[-1], '.r')
    fig.savefig('day10.png')
    if close:
        plt.close(fig)
    else:
        return fig, ax

def visualize_set(df, start, n):
    for i in range(n):
        fig, ax = plt.subplots(figsize=(19.2,10.8))
        ax.plot(df['x'][start+i], df['y'][start+i], '.')
        ax.set_ylim(df['y'][start].min(), df['y'][start].max())
        ax.set_xlim(df['x'][start].min(), df['x'][start].max())
        file = 'day10_{}.png'.format(start+i)
        fig.savefig(file)
        print('saved to {}'.format(file))
        plt.close(fig)

def determine_extents(x, y, x_vel, y_vel):
    df = pd.DataFrame({
        'x': x,
        'y': y,
        'x_vel': x_vel,
        'y_vel': y_vel
    })
    x1 = df.min()['x']
    x2 = df[df['x'] < 0]['x'].max()
    x3 = df[df['x'] > 0]['x'].min()
    start = abs(x1 - x2) / df['x_vel'].max()
    end = abs(x1 - x3) / df['x_vel'].max()
    return start, end

def bounding_box(x, y):
    size = (
        x.max() - x.min(),
        y.max() - y.min()
    )
    return size[0] * size[1]

def make_dfs(input, n=None):
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

    # construct position over time df
    if n is None:
        n = determine_extents(x, y, x_vel, y_vel)
    elif isinstance(n, tuple):
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
    pos_df['y'] = df.multiply(y_vel, axis=0).add(y, axis=0) * -1

    return pos_df

def part1(input):
    dfp = make_dfs(input)

    prev_bb = 0
    for i, col in dfp['x'].iteritems():
        bb = bounding_box(col, dfp['y'][i])
        if bb > prev_bb and prev_bb != 0:
            break
        prev_bb = bb
    # visualize_set(dfp, i - 5, 10)
    # visualize(dfp, i-1)
    return

def part2(input):
    dfp = make_dfs(input)

    prev_bb = 0
    for i, col in dfp['x'].iteritems():
        bb = bounding_box(col, dfp['y'][i])
        if bb > prev_bb and prev_bb != 0:
            break
        prev_bb = bb
    return i

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))