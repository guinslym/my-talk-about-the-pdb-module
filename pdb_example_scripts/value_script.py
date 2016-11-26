import code
import runpy
from my_other_script import students_list


def divide(denominator=2, students=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    list_num = []
    for value in [3,2,1]:
        denominator *= value
        answer = 10 / denominator
        list_num.append(answer)
    return list_num

if __name__ == "__main__":
    import pdb
    pdb.runcall(divide)



