from functools import cache

FILE = "./input14.txt"
#FILE = "./test14.txt"
#FILE = "./test142.txt"

def lire(fic):
    with open(FILE, "rt") as text:
        mat = []
        for j, l in enumerate(text.read().splitlines()):
            row = []
            for i,c in enumerate(l):
                row.append(c)
            mat.append(tuple(row))
        return tuple(mat)


def rot_a(it):
    return tuple(zip(*it))

def rotate(it):
    return tuple(zip(*it[::-1]))


def columns(it):
    return tuple(rotate(list(it[::-1])))

def tilt(it):
    res = []
    for s in [ ''.join(c) for c in columns(it)]:
        new_col = []
        for x in s.split('#'):
            co, cd = x.count('O'), x.count('.')
            new_col.append('O' * co + '.' * cd)
        res.append(tuple( [c for c in  '#'.join(new_col)]))
    return rotate(tuple(res[::-1]))

def score(it):
    res = 0
    v = len(it)
    for r in it:
        res += r.count('O') * v
        v -= 1
    return res

def dump(it, msg= " "):
    print(msg)
    for i,x in enumerate(it):
        print(f"{i}\t{' '.join(x)}")
def part1():
    rocks = lire(FILE)
    tlt = tilt(rocks)
    print(score(tlt))

def part2(n):
    seen = {}
    rocks = lire(FILE)

    xx = list(rocks)
    for _ in range(n):
        k = tuple(xx)
        xx = list(one_cycle(k))
        if not k in seen:
            res = score(k)
            seen[k] = {'n': _, 'score': res}
            print(_, seen[k])
        else:
            print(f"step {_} deja vu {seen[k]} / {len(seen)}")
            # dump(xx, f"step {_} deja vu {seen[k]} / {len(seen)}")


    dump(xx, f"cycle {_ +1}")

@cache
def one_cycle(it):

    t0 = rotate(tilt(it))
    t1 = rotate(tilt(t0))
    t2 = rotate(tilt(t1))
    t3 = rotate(tilt(t2))

    return t3

if __name__ == '__main__':
    # part1()
    #part2(1_00)

    #part2(1_000_000_000)
    part2(200)
    # res = rotate(tlt)
    #dump(res, "rotate")
