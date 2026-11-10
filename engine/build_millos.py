"""millos-pizza-and-grill-barrington: plain template, own palette from clients/millos-pizza-and-grill-barrington/data.json. usage: build_millos.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('millos-pizza-and-grill-barrington', ['Pizza','Greek','Subs'])
