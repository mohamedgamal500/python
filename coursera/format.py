inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99",
             "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    item_l = item.split(",")
    print(f'The store has {item_l[1]} {item_l[0]}, each for {item_l[2]} USD.')
    my_string = "The store has {} {}, each for {} USD."
    print(my_string.format(item_l[1], item_l[0], item_l[2]))
