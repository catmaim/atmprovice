
import os

filepath = 'js.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'CustomStatusSelect' in line or 'Icons' in line:
        print(f"Line {i+1}: {line.strip()}")
