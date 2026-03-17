
import os

def fix_mojibake(filepath):
    print(f"Checking {filepath}...")
    try:
        with open(filepath, 'rb') as f:
            bytes_content = f.read()
        
        # Original content was UTF-8. 
        # It was misinterpreted as Windows-1252 (cp1252) and then saved as UTF-8.
        # So we decode as UTF-8 to get the 'à¸' string, then encode as cp1252 to get the original bytes.
        text = bytes_content.decode('utf-8')
        
        # Try to recover bytes. Use 'replace' for safety, but hopefully 'cp1252' matches.
        # The character \u20ac is what tipped us off to cp1252.
        recovered_bytes = text.encode('cp1252', errors='replace')
        
        # Now decode correctly as UTF-8
        try:
            final_text = recovered_bytes.decode('utf-8')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_text)
            print(f"SUCCESS: {filepath}")
        except Exception as e:
            print(f"RECOVERY FAILED for {filepath}: {e}")
            
    except Exception as e:
        print(f"ERROR processing {filepath}: {e}")

fix_mojibake('js.txt')
fix_mojibake('code gs.txt')
print("Done.")
