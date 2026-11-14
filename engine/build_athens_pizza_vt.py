"""athens-pizza-vt: plain template, own palette from clients/athens-pizza-vt/data.json. usage: build_athens_pizza_vt.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('athens-pizza-vt', ['Pizza','Subs','Italian'])
