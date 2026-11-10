"""fire-21-pizza-conway: plain template, own palette from clients/fire-21-pizza-conway/data.json. usage: build_fire21.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('fire-21-pizza-conway', ['Subs','Pizza','Pasta'])
