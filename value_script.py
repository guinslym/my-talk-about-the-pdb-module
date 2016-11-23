import code
import runpy
from my_other_script import students_list


def divide(denominator=2, other_val=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    num_list = []
    for value in [3,2,1,1]:
        denominator *= value
        answer = 10 / denominator
        num_list.append(answer)
    return num_list

if __name__ == "__main__":
    import pdb
    pdb.runcall(divide)



