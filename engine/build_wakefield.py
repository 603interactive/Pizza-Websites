"""wakefield-house-of-pizza: plain template, own palette from clients/wakefield-house-of-pizza/data.json. usage: build_wakefield.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('wakefield-house-of-pizza', ['Pizza','Subs','Italian'])
