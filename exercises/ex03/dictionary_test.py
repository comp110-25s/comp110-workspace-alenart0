"""Exercise 3 Dictionary Test"""

__author__ = "730571229"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest

"""Invert Automated Tests"""


def test_invert_empty_dict():
    """
    Test inversion of an empty dictionary,
    with an empty dictionary as ideal result
    """
    assert invert({}) == {}


def test_invert_normal_dict1():
    """
    Test for use case 1,
    Ideal result is inverted keys and values
    """
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


def test_invert_normal_dict2():
    """
    Test for use case 2,
    Ideal result is inverted keys and values
    """
    assert invert({"Anne": "pink", "Ben": "blue", "Colin": "green"}) == {
        "pink": "Anne",
        "blue": "Ben",
        "green": "Colin",
    }


with pytest.raises(KeyError):
    my_dictionary = {"a": "1", "b": "1"}
    invert(my_dictionary)

"""Count Automated Tests"""


def test_count_empty_list():
    assert count([]) == {}


def test_count_use_case1():
    assert count(["pink", "pink", "blue"]) == {"pink": 2, "blue": 1}


def test_count_use_case2():
    assert count(["a", "b", "a", "a", "b"]) == {"a": 3, "b": 2}


"""Favorite_color Automated tests"""


"""Bin_len automated tests"""


def test_bin_len_empty_set():
    assert bin_len([]) == {}


def test_bin_len_use_case1():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case2():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
