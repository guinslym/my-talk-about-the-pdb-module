import code
import runpy
import shlex
from ptpdb import set_trace
from my_other_script import students_list

def divide(denominator=2, other_val=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    list_num = []
    set_trace()
    for value in [3,2,1,0]:
        denominator *= value
        answer = 10 / denominator
        list_num.append(answer)
    return list_num

if __name__ == "__main__":
    list_of_numbers = divide()




