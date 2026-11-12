"""st-johnsbury-house-of-pizza-vt: plain template, own palette from clients/st-johnsbury-house-of-pizza-vt/data.json. usage: build_st_johnsbury_house_of_pizza_vt.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('st-johnsbury-house-of-pizza-vt', ['Pizza','Subs','Italian'])
