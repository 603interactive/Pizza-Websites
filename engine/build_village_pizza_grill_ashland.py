"""village-pizza-grill-ashland: plain template, own palette from clients/village-pizza-grill-ashland/data.json. usage: build_village_pizza_grill_ashland.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('village-pizza-grill-ashland', ['Pizza','Subs','Italian'])
