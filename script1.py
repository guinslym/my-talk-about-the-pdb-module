import code
import runpy
import shlex
from my_other_script import students_list

def divide(denominator=2, other_val=students_list):
    """
    divide 10 by a given number
    """
    num_list = []
    for value in [3,2,1,0]:
        denominator *= value
        answer = 10 / denominator
        num_list.append(answer)
    return num_list

if __name__ == "__main__":
    list_of_numbers = divide()



