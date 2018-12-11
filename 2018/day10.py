import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize(pos_df, n, fig=None, ax=None, close=True):
    df = pos_df[n]
    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(19.2, 10.8))
    ax.plot(df, '.')
    fig.savefig('day10.png')
    if close:
        plt.close(fig)
    else:
        return fig, ax

def make_dfs(input, n=1000):
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
    vel_df = pd.DataFrame({'x': x_vel, 'y': y_vel})

    # construct position over time df
    idx = pd.MultiIndex.from_product([['x', 'y'], np.arange(n)])
    pos_df = pd.DataFrame(columns=idx, index=np.arange(length))
    for (axis, t), values in pos_df.iteritems():
        if axis == 'x':
            pos_df.loc[:, (axis, t)] = x + (t * x_vel)
        elif axis == 'y':
            pos_df.loc[:, (axis, t)] = y + (t * y_vel)

    return pos_df

def part1(input):
    dfp = make_dfs(input, n=5000)
    visualize(dfp, 1000)
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))