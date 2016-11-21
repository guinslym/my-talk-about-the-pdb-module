import shlex
import sys
from my_other_script import students_list


def divide(denominator=2, other_val=students_list):
    return 10 / denominator

def calling_the_divide_function(value=4):
    val = []
    for i in value:
        a = divide(i)
        val.append(a)
    return val

def create_a_list_of_numbers(value=5):
    value = list(range(9))
    #reversing the list
    value = value[::-1]
    calling_the_divide_function(value)

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    create_a_list_of_numbers()



