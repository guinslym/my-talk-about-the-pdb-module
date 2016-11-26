#python post_mortem_script1.py
def divide(denominator=2):
    """
    dummy function that divide 10 by a given number
    return: a list
    """
    list_num = []
    for value in [3,2,1,0]:
        denominator *= value
        answer = 10 / denominator
        list_num.append(answer)
    return list_num

if __name__ == "__main__":
    try:
        list_of_numbers = divide()
    except:
        import pdb; pdb.post_mortem()




