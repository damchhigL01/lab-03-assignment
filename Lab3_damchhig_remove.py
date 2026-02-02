"""
Program Name: Remove Camping Item
Author: Damchhig Lama
Purpose: Remove binoculars from the list and display
the final packing list and total item count.
Starter Code: Imported from Lab3_damchhig_replace.py
Date: February 01, 2026
"""

from Lab3_damchhig_replace import camping_items

camping_items.remove("binoculars")

print("Final camping list:")
print(camping_items)

print(f"Total items being brought: {len(camping_items)}")
