import sys
from pathlib import Path

p = Path(__file__)
con = str(p.parents[1])
sys.path.insert(0, con)

import aoc_input
import day3
import day10
import day12
