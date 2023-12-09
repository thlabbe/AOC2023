import re

FILE = "./input9.txt"
FILE = "./test9.txt"

def load():
    with open(FILE, "rt") as text:
        return text.readlines()

def prep1(lines):
    seqs = [list(map(int, re.findall(r"-?\w+", l))) for l in lines]
    return seqs

def is_constant(l):
    return len(set(l)) == 1


def find_next(l):
    if is_constant(l):
        return l[0]
    else:
        x = l[-1] + find_next([l[i + 1]
                                  - l[i]
                                  for i in range(len(l) - 1)])
        print(x)
        return x

def find_prev(l):
    if is_constant(l):
        return l[0]
    else :
        return l[0] - find_prev([l[i + 1]
                                 - l[i]
                                 for i in range(len(l) - 1)])


data = prep1(load())
print(sum(find_next(l) for l in data))
print(sum(find_prev(l) for l in data))