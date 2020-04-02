import sys


class Mutable():
    def __init__(self, num):
        self.num = num


def convertDigit(mut, base):
    mod = mut.num % base
    mut.num = mut.num // base
    return mod
    pass


def convertNumber(mut, base):
    newnum = []
    while mut.num >= base:
        mod = convertDigit(mut, base)
        newnum.insert(0, mod)
    newnum.insert(0, mut.num)
    newnum = digitManip(newnum, base)
    strings = [str(intt) for intt in newnum]
    return "".join(strings)
    pass


def digitManip(numlist, base):
    size = len(numlist)

    for i in range(size):
        if numlist[i] < base and numlist[i] > 9:
            numlist[i] = chr(ord('A') + (numlist[i] % 10))
    return numlist


if __name__ == "__main__":
    args = sys.argv[2:]
    base = int(sys.argv[1])
    if base > 20:
        base = 20
    elif base < 2:
        base = 2

    for i in args:
        numM = Mutable(int(i))
        print(i, end=" = ")
        print(convertNumber(numM, base))
