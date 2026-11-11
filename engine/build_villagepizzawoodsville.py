"""village-pizza-woodsville: plain template, own palette from clients/village-pizza-woodsville/data.json. usage: build_villagepizzawoodsville.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('village-pizza-woodsville', ['Pizza'])
