
import os

filepath = 'js.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

def find_syntax_issues(s):
    i = 0
    stack = []
    issues = []
    line = 1
    col = 1
    
    while i < len(s):
        c = s[i]
        
        if c == '\n':
            line += 1
            col = 1
        else:
            col += 1

        if not stack:
            if c in ['"', "'", '`']:
                stack.append((c, line, col, i))
        else:
            top_q, top_l, top_c, top_i = stack[-1]
            if c == top_q:
                # Check for escape
                bs_count = 0
                j = i - 1
                while j >= 0 and s[j] == '\\':
                    bs_count += 1
                    j -= 1
                if bs_count % 2 == 0:
                    stack.pop()
            elif c == '\n' and top_q != '`':
                # Unterminated string on line
                issues.append(f"Unterminated {top_q} at line {top_l}, col {top_c}")
                stack.pop()
        
        i += 1
    
    for q, l, c, _ in stack:
        issues.append(f"Unclosed {q} starting at line {l}, col {c}")
    return issues

issues = find_syntax_issues(text)
if issues:
    for iss in issues:
        print(iss)
else:
    print("No obvious unclosed strings found.")
