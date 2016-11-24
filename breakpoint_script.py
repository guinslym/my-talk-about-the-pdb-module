import code
import runpy
import shlex
from my_other_script import students_list


def sentences():
    """
    dummy function that returns the last value of a split sentence
    """
    value = 'Meetup'
    a,b,c,d = shlex.split("This is the 'OPAG meetup'")
    return d.upper()

def divide(denominator=2, other_val=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    list_num = []
    compteur = 0 
    for value in range(2000, 0, -1):
        denominator *= value
        answer = 10 / denominator
        list_num.append(answer)
        compteur += 1
    my_sentence = sentences()
    return list_num

if __name__ == "__main__":
    divide()
