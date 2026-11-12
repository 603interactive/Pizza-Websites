"""supreme-house-of-pizza-hooksett: plain template, own palette from clients/supreme-house-of-pizza-hooksett/data.json. usage: build_supreme_house_of_pizza_hooksett.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('supreme-house-of-pizza-hooksett', ['Pizza','Subs','Italian'])
