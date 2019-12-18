import sys
from pathlib import Path

p = Path(__file__)
con = str(p.parents[2])
sys.path.insert(0, con)

import intcode
