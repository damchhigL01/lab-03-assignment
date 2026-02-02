"""
Program Name: Add Camping Items
Author: Damchhig Lama
Purpose: Import an existing camping list and add more items,
then display the list in reverse alphabetical order.
Starter Code: Imported from Lab3_damchhig_list.py
Date: February 01, 2026
"""

from Lab3_damchhig_list import camping_items

camping_items.append("hat")
camping_items.append("extra socks")
camping_items.append("sunscreen")
camping_items.append("phone charger")
camping_items.append("rain poncho")

print("Reversed alphabetical list:")
print(sorted(camping_items, reverse=True))
