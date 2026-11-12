"""nikos-waterville-house-of-pizza-me: plain template, own palette from clients/nikos-waterville-house-of-pizza-me/data.json. usage: build_nikos_waterville_house_of_pizza_me.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('nikos-waterville-house-of-pizza-me', ['Pizza','Subs','Italian'])
