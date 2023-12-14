FILE = "./input14.txt"
FILE = "./test14.txt"

#FILE = "./test142.txt"

def load():
    mat = []

    with open(FILE, "rt") as text:
        for j,r in  enumerate((text.readlines())):
            row =[]
            for i,c in enumerate(r):
                if c != '\n':
                    row.append(c)
            mat.append(tuple(row))
    return tuple(mat)


def rotate(mat):
    "-90°"
    return list(zip(*mat[::-1]))


def get_cols(mat):
    res = []
    tmp = rotate(mat)
    for i in range(len(tmp)):
        res.append(tmp[i][::-1])
    return res

def tilt(c):
    res = []
    s = ''.join(c)
    t = s.split('#')
    for x in t:
        co = x.count('O')
        cd = x.count('.')
        nl = 'O' * co + '.' * cd
        res.append(nl)
    return [c for c in '#'.join(res)]

def cycle(mat):
    print("cycle")
    dump(mat)


    north = tilt_1(mat)
    print("north1")
    dump(north)
    print("rot nort")
    dump(rotate(north))
    west = tilt_1(rotate3(north))
    print("west")
    dump(west)
    south = tilt_1(rotate3(west))
    print("south")
    dump(south)
    east = tilt_1(rotate3(west))
    print("east")
    dump(east)

    return east
def tilt_1(mat):
    cols = get_cols(mat)
    tilted = []
    for i, c in enumerate(cols):
        tilted.append(tilt(c))

    return tilted

def dump(m):
    for i,l in enumerate(m): print(i,l)

def rotate3(mat):
    return rotate(rotate(rotate(mat)))

if __name__ == '__main__':
    mat = load()
    cols = get_cols(mat)
    v = []
    for i in range(len(cols[0]),0, -1):
        v.append(i)

    tilted = cycle(mat)
    res = 0
    for i,l in enumerate(rotate(tilted)):
        score = v[i] * l.count('O')
        res += score
    print(res)
    dump(tilted)
