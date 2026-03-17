
import os

filepath = 'js.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def count_unescaped(s, quote):
    count = 0
    i = 0
    while i < len(s):
        if s[i] == quote:
            bs_count = 0
            j = i - 1
            while j >= 0 and s[j] == '\\':
                bs_count += 1
                j -= 1
            if bs_count % 2 == 0:
                count += 1
        i += 1
    return count

total_sq = 0
for i, line in enumerate(lines):
    sq = count_unescaped(line, "'")
    total_sq += sq
    if sq % 2 != 0:
        # Ignore lines that are clearly not the start of a multi-line string
        # though JS doesn't support them except backticks.
        print(f"BINGO: Line {i+1} has odd single quotes ({sq}): {line.strip()}")

print(f"Total single quotes: {total_sq}")
