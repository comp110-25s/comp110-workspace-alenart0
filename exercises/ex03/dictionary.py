"""Exercise 3 dictionary"""

__author__ = "730571229"


def invert(d: dict[str, str]):
    inverted_dict = {}
    for k, v in d.items():
        if v in inverted_dict:
            raise KeyError("value is a duplicate")
        inverted_dict[v] = k
    print(inverted_dict)


def count(lname: list[str]) -> dict[str, int]:
    result_dict = {}
    for item in lname:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def favorite_color(cdict: dict[str, str]) -> str:

    colors = list(cdict.values())
    color_count = count(colors)
    return max(color_count, key=color_count.get)


def bin_len(str_list: list[str]) -> dict[int, set[str]]:
    length_dict = {}

    for str in str_list:
        str_length = len(str)

        if str_length not in length_dict:
            length_dict[str_length] = set()

        length_dict[str_length].add(str)

    return length_dict
