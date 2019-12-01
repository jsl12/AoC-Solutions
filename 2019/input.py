import config
from pathlib import Path

p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark')
cfg = config.Config(p / 'users.yaml')

def day_gen(day_num:int):
    file = [f for f in cfg.inputs_dir.glob(f'2019/*day{day_num}.txt')][0]
    print(f'Getting input for 2019 Day {day_num} from:\n{file}')
    with file.open('r') as f:
        return (line for line in f.readlines())
