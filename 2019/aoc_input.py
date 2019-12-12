import logging
from pathlib import Path

import config

cfg = config.Config(r'D:\AoC\users.yaml')

logger= logging.getLogger( __name__ )

def find_input(day_num:int) -> Path:
    file = [f for f in cfg.inputs_dir.glob(f'2019/*day{day_num}.txt')][0]
    logger.debug(f'Got input from:\n{file}')
    return file


def gen(day_num:int):
    file = find_input(day_num)
    with file.open('r') as f:
        return (line for line in f.readlines())


def read(day_num: int):
    file = find_input(day_num)
    with file.open('r') as f:
        return f.read()
