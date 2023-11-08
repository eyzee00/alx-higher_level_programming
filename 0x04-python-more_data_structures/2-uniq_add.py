#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:
        return 0
    unique_list = []
    for element in my_list:
        if unique_list == []:
            unique_sum = element
            unique_list.append(element)
        else:
            unique = True
            for i in unique_list:
                if i == element:
                    unique = False
                    break
            if unique:
                unique_sum += element
                unique_list.append(element)
    return unique_sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
