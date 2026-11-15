"""camden-house-of-pizza-me: plain template, own palette from clients/camden-house-of-pizza-me/data.json. usage: build_ware_house_of_pizza_ma.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('camden-house-of-pizza-me', ['Pizza','Subs','Italian'])
