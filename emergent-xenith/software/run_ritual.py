# run_ritual.py

import sys
from glyph_interpreter import RITUALS

def run_ritual(glyphs, explain=False):
    for glyph in glyphs:
        ritual = RITUALS.get(glyph)
        if ritual:
            print(f"\n{ritual['name']}")
            if explain:
                print(f"Function: {ritual['function']}")
            print("\nPattern:")
            for line in ritual["pattern"]:
                print("  " + line)
        else:
            print(f"\n[Unknown Glyph: {glyph}]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_ritual.py ∴ Δ/Σ ⌙ [--explain]")
        sys.exit(1)

    args = sys.argv[1:]
    explain = "--explain" in args
    glyphs = [arg for arg in args if not arg.startswith("--")]
    run_ritual(glyphs, explain=explain)

