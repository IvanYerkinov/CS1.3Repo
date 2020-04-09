import sys


def genfib(n1, n2):
    return n1 + n2


def generator(num):
    valueReturn = 0
    n2 = 0
    n1 = 1
    for i in range(num):
        valueReturn = genfib(n1, n2)
        n2 = n1
        n1 = valueReturn
    return valueReturn


def recursiveGen(num, n1=1, n2=0):
    if num <= 1:
        return n1 + n2
    value = recursiveGen(num-1, n1+n2, n1)
    return value


if __name__ == "__main__":
    print(generator(int(sys.argv[1])))
    print(recursiveGen(int(sys.argv[1])))
    pass
