import config
from pathlib import Path

p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark')
cfg = config.Config(p / 'users.yaml')

def read(i):
    file = [f for f in cfg.inputs_dir.glob('2019/*day{}.txt'.format(i))][0]
    print('Getting input for 2018 Day {} from:\n{}'.format(i, file))
    with open(file, 'r') as f:
        return f.read()