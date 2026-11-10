"""family-pizza-pittsfield: plain template, own palette from clients/family-pizza-pittsfield/data.json. usage: build_familypizza.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('family-pizza-pittsfield', ['Pizza','Subs','Italian'])
