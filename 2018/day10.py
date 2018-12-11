import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize(pos_df, close=True):
    df = pos_df.set_index('x').sort_index()
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    ax.plot(df, '.')
    fig.savefig('day10.png')
    if close:
        plt.close(fig)
    else:
        return fig, ax

def make_dfs(input):
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
    pos_df = pd.DataFrame({'x': x, 'y': y})
    vel_df = pd.DataFrame({'x': x_vel, 'y': y_vel})
    return pos_df, vel_df

def part1(input):
    dfp, dfv = make_dfs(input)

    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))