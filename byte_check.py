
import os

filepath = 'js.txt'
with open(filepath, 'rb') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if b'REGION_8_PROVINCES' in line:
        print(f"Line {i+1} bytes: {line}")
        break
