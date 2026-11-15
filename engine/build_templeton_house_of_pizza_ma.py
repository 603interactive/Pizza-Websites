"""templeton-house-of-pizza-ma: plain template, own palette from clients/templeton-house-of-pizza-ma/data.json. usage: build_ware_house_of_pizza_ma.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('templeton-house-of-pizza-ma', ['Pizza','Subs','Italian'])
