import config
from pathlib import Path

p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark')
cfg = config.Config(p / 'users.yaml')

def read(i):
    file = [f for f in cfg.inputs_dir.glob('2018/*day*{}.txt'.format(i))][0]
    with open(file, 'r') as f:
        return f.read()