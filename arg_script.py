import sys

def divide(numerator, denominator):
    return numerator / denominator

if __name__ == '__main__':
    numerator = int(sys.argv[1])
    denominator = int(sys.argv[2])
print( divide(numerator, denominator))