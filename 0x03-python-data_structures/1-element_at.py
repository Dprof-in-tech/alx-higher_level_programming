#!/usr/bin/python3
def element_at(my_list, idx):
    integers = my_list
    int_idx = integers[idx]
    if int_idx < 0:
        return None
    elif int_idx > len(integers):
        return None
    else:
        return int_idx
