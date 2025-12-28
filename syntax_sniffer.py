#!/usr/bin/env python3
# Syntax Sniffer: The Code Smell Detector
# Because your code smells worse than week-old pizza

import re
import sys
from pathlib import Path

def sniff_file(filepath):
    """Sniffs out code smells like a truffle pig in a garbage dump"""
    smells = []
    
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Failed to read file: {e}"]
    
    for i, line in enumerate(lines, 1):
        # Sniff 1: Trailing whitespace (the silent killer)
        if line.rstrip() != line.rstrip('\n'):
            smells.append(f"Line {i}: Trailing whitespace - like leaving socks on the floor")
        
        # Sniff 2: Tab characters (the forbidden fruit)
        if '\t' in line:
            smells.append(f"Line {i}: Tab character detected - are you coding in 1995?")
        
        # Sniff 3: Really long lines (the never-ending story)
        if len(line.rstrip()) > 100:
            smells.append(f"Line {i}: Line too long ({len(line.rstrip())} chars) - even novels have paragraphs")
        
        # Sniff 4: TODO comments (the eternal promise)
        if 'TODO' in line.upper():
            smells.append(f"Line {i}: TODO found - we both know this will never get done")
        
        # Sniff 5: Print statements in production (the cry for help)
        if re.search(r'print\(', line) and not re.search(r'#.*debug', line.lower()):
            smells.append(f"Line {i}: Print statement - the poor man's debugger")
    
    # Sniff 6: File too big (the kitchen sink approach)
    if len(lines) > 500:
        smells.append(f"File too long ({len(lines)} lines) - maybe split it? Just a thought...")
    
    return smells

def main():
    """Main function - because every script needs one, apparently"""
    if len(sys.argv) < 2:
        print("Usage: python syntax_sniffer.py <file_or_directory>")
        print("Example: python syntax_sniffer.py my_ugly_code.py")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    files_to_sniff = []
    
    if target.is_file():
        files_to_sniff = [target]
    elif target.is_dir():
        files_to_sniff = list(target.rglob("*.py"))
    else:
        print(f"Target '{target}' not found - did you dream this file?")
        sys.exit(1)
    
    total_smells = 0
    for filepath in files_to_sniff:
        smells = sniff_file(filepath)
        if smells:
            print(f"\n🔍 Sniffing {filepath}:")
            for smell in smells:
                print(f"  👃 {smell}")
                total_smells += 1
    
    if total_smells:
        print(f"\n🎉 Found {total_smells} code smells! Your code needs a shower.")
    else:
        print("\n✨ No smells detected! Either your code is perfect or the sniffer is broken.")

if __name__ == "__main__":
    main()
