"""lewiston-house-of-pizza-me: plain template, own palette from clients/lewiston-house-of-pizza-me/data.json. usage: build_lewiston_house_of_pizza_me.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('lewiston-house-of-pizza-me', ['Pizza','Subs','Italian'])
