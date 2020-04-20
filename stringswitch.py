import sys


def stringswitch(str):
    newstring = []
    for i in str:
        newstring.insert(0, i)
    return "".join(newstring)


if __name__ == "__main__":
    print(stringswitch(sys.argv[1]))
