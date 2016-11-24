import code
import shlex
import runpy
from my_other_script import students_list

def sentences():
    value = 'Meetup'
    a,b,c,d = shlelx.split("This is the 'OPAG meetup'")
    return d.upper()

def divide(denominator=2, other_val=students_list):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    list_num = []
    compteur = 0 
    for value in range(2000):
        denominator *= value
        answer = 10 / denominator
        list_num.append(answer)
        compteur += 1
    my_sentence = sentences()
    return list_num

if __name__ == "__main__":
    divide()
