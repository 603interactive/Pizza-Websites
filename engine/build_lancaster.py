"""lancaster-house-of-pizza-lancaster: plain template, own palette from clients/lancaster-house-of-pizza-lancaster/data.json. usage: build_lancaster.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('lancaster-house-of-pizza-lancaster', ['Pizza','Grinders','Wraps'])
