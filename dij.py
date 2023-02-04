list_items = [1,2,3,4,5,6]
item_to_search = 4
while True:
    low_pointer = list_items[0]
    high_pointer = list_items[-1]
    mid_point = (list_items.index(low_pointer) + list_items.index(high_pointer)) // 2
    print(mid_point)