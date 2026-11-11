"""jimmys-hometown-pizzeria: plain template, own palette from clients/jimmys-hometown-pizzeria/data.json. usage: build_jimmyshometown.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('jimmys-hometown-pizzeria', ['Pizza','Subs','Italian'])
