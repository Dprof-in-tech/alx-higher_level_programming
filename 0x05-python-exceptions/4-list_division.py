#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if isinstance(my_list_1[i], (int, float)):
                if my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                result = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError("wrongtype")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        finally:
            new_list.append(result)
    return new_list
