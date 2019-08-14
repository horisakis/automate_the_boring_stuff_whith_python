def display_inventory(inventory):
  print("持ち物リスト")
  item_total = 0
  for k, v in inventory.items():
    print(str(v) + " " + k)
    item_total += v
  print("アイテム総数： " + str(item_total))

def add_to_inventory(inventory, added_items):
  for k in added_items:
    inventory.setdefault(k, 0)
    inventory[k] += 1
  return inventory

inv = {"金貨": 42, "ロープ": 1}
doragon_loot = ["金貨", "手裏剣", "金貨", "金貨", "ルビー"]
inv = add_to_inventory(inv, doragon_loot)
display_inventory(inv)
