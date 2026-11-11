"""plymouth-house-of-pizza-ma: plain template, own palette from clients/plymouth-house-of-pizza-ma/data.json. usage: build_plymouthhop.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('plymouth-house-of-pizza-ma', ['Pizza','Greek','Pub'])
