"""pizzeria-roma-milford: plain template, own palette from clients/pizzeria-roma-milford/data.json. usage: build_roma.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('pizzeria-roma-milford', ['Pizza','Italian','Subs'])
