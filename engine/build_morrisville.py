"""morrisville-house-of-pizza-vt: plain template, own palette from clients/morrisville-house-of-pizza-vt/data.json. usage: build_morrisville.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_plainshop import run
run('morrisville-house-of-pizza-vt', ['Pizza','Subs','Italian'])
