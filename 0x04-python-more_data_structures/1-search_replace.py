#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element is not search:
            new_list.append(element)
        else:
            new_list.append(replace)
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
