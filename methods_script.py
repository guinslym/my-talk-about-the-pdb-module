import code
import runpy
import shlex
from my_other_script import students_list
import pdb

pdb.run('my_module')

def divide(denominator=2, other_val=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    num_list = []
    for value in [3,2,1]:
        pdb.set_trace()
        answer = 10 / denominator
        num_list.append(answer)
    return num_list

if __name__ == "__main__":
    pdb.runcall(divide)
    list_of_numbers = divide()
    pdb.runeval("[x / 1 for x in range(3)]")




