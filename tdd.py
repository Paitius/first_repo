from functions import *


def multiply_test():
    assert multiply(5,10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5,1.5) == 2.25

def no_of_letter_test():
    assert no_of_letter('kamil') == 5
    assert no_of_letter('') == 0