"""
Program Name: Replace Camping Item
Author: Damchhig Lama
Purpose: Replace one camping item with binoculars
and display the list using slicing.
Starter Code: Imported from Lab3_damchhig_add.py
Date: February 01, 2026
"""

from Lab3_damchhig_add import camping_items

camping_items[5] = "binoculars"

index = camping_items.index("binoculars")

print("Before binoculars:")
print(camping_items[:index])

print("Binoculars:")
print(camping_items[index])

print("After binoculars:")
print(camping_items[index + 1:])
