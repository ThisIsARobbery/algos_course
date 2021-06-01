
def pack_backpack(w_backpack, items):
    total_c = 0.0
    used_w = 0
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    i = 0
    while used_w < w_backpack and i < len(items):
        item_c = items[i][0]
        item_w = items[i][1]
        if w_backpack - used_w >= item_w:
            total_c += item_c
            used_w += item_w
        else:
            total_c += item_c * ((w_backpack - used_w) / item_w)
            used_w += w_backpack - used_w
        i += 1
        
    print("{:.3f}".format(total_c))

first_str = input().split(" ")
n_items = int(first_str[0])
w_backpack = int(first_str[1])
items = []
for _ in range(n_items):
    item_str = input().split(" ")
    items.append([float(item_str[0]), float(item_str[1])])

pack_backpack(w_backpack, items)
