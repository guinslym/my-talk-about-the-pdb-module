import code
import shlex
import runpy
from my_other_script import students_list

def sentences():
    a,b,c,d = shlex.split("This is the 'OPAG meetup'")
    return d.upper()

def divide(denominator=2, other_val=students_list):
    """
    divide 10 by a given number
    """
    num_list = []
    for value in [3,2,1]:
        denominator *= value
        answer = 10 / denominator
        num_list.append(answer)
    my_sentence = sentences()
    return num_list

if __name__ == "__main__":
    divide()
