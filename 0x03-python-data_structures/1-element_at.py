#!/usr/bin/python3
def element_at(my_list, idx):
    integers = my_list
    int_idx = integers[idx]
    if idx < 0:
        return None
    elif idx > len(integers):
        return None
    else:
        return int_idx
