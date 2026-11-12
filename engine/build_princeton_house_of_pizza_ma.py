"""princeton-house-of-pizza-ma: plain template, own palette from clients/princeton-house-of-pizza-ma/data.json. usage: build_princeton_house_of_pizza_ma.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('princeton-house-of-pizza-ma', ['Pizza','Subs','Italian'])
