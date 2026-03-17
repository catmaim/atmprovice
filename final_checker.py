
import os

filepath = 'js.txt'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count braces, parens, brackets
    print(f"Braces: {content.count('{')} open, {content.count('}')} close (Diff: {content.count('{') - content.count('}')})")
    print(f"Parens: {content.count('(')} open, {content.count(')')} close (Diff: {content.count('(') - content.count(')')})")
    print(f"Brackets: {content.count('[')} open, {content.count(']')} close (Diff: {content.count('[') - content.count(']')})")
    
    # Simple quote check (not perfect due to escapes, but helpful)
    # Filter out escaped quotes
    def count_unescaped(s, quote):
        count = 0
        i = 0
        while i < len(s):
            if s[i] == quote:
                # Check if preceded by odd number of backslashes
                bs_count = 0
                j = i - 1
                while j >= 0 and s[j] == '\\':
                    bs_count += 1
                    j -= 1
                if bs_count % 2 == 0:
                    count += 1
            i += 1
        return count

    dq = count_unescaped(content, '"')
    sq = count_unescaped(content, "'")
    bt = count_unescaped(content, "`")
    
    print(f"Double Quotes: {dq} (Modulo 2: {dq % 2})")
    print(f"Single Quotes: {sq} (Modulo 2: {sq % 2})")
    print(f"Backticks: {bt} (Modulo 2: {bt % 2})")

    # Specifically check for common GAS HtmlService issue: script tag inside
    if "</script>" in content[:-10]: # Exclude the very end
        print("WARNING: Possible </script> tag detected inside the JS code!")
