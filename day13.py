


FILE = "./input13.txt"
# FILE = "./test13.txt"


def load():
    with open(FILE, "rt") as text:
        return text.readlines()


def process(lst):
    res = []
    mat = []
    for l in lst:

        if len(l) > 1:
            r = []
            for c in l:
                if c != '\n': r.append(c)
            mat.append(r)
        else:
            res.append(mat)
            mat = []
    res.append(mat)

    return res



def rotate(mat):
    return list(zip(*mat))

def debug(matrices):
    for j,m in enumerate(matrices): # m = matrices[0]
        print("original")
        for i,r in enumerate(m): print(j, i, " ", r)
        m2 = rotate(m)
        print("rotate")
        for i,r in enumerate(m2): print(j, i, " ", r)

def dump(m):
    for i,r in enumerate(m):
        print(i,'\t', r)

def compare(v1 , v2):
    cnt = 0
    for i,a in enumerate(v1):
        b = v2[i]
        if a != b : cnt += 1
    return cnt
def is_mirror_smudged(i, m, rows):
    diff = 0
    if i >= rows : # ne pas tester les bords
        return False

    mirror = True

    for d in range(rows + 1):
        a = i + d + 1
        b = i - d
        if not mirror:
            return mirror
        if (mirror
                and a >= 0
                and a <= rows
                and b >= 0
                and b <= rows):
            diff += compare(m[a], m[b])
            mirror = mirror and ( diff<=1 )
    return mirror and diff == 1

def is_mirror(i, m, rows):
    if i >= rows : # ne pas tester les bords
        return False

    mirror = True

    for d in range(rows + 1):
        a = i + d + 1
        b = i - d
        if not mirror:
            return mirror
        if (mirror
                and a >= 0
                and a <= rows
                and b >= 0
                and b <= rows):
            mirror = mirror and m[a] == m[b]
    return mirror
def duplicate_adj2(m):
    rows_candidate = []
    rows = len(m) -1
    for i,r in enumerate(m):
        if is_mirror_smudged(i,m, rows):
            print('row', i + 1, rows_candidate)
            rows_candidate.append(i + 1)


    cols_candidate = []

    m = rotate(m)
    rows = len(m) - 1
    for i,r in enumerate(m):
        if is_mirror_smudged(i, m, rows):
            print('col', i + 1, cols_candidate)
            cols_candidate.append(i + 1)

    res = {'cols': cols_candidate, 'rows': rows_candidate}
    return res

def duplicate_adj(m):
    res ={}
    rows_candidate = []
    rows = len(m) -1
    for i,r in enumerate(m):
        if is_mirror(i,m, rows):
            rows_candidate.append(i + 1)


    cols_candidate = []

    m = rotate(m)
    rows = len(m) - 1
    for i,r in enumerate(m):
        if is_mirror(i, m, rows):
            cols_candidate.append(i + 1)
    res = {'cols' : cols_candidate, 'rows' : rows_candidate}
    return res

if __name__ == '__main__':
    entree = load()
    print(len(entree))
    matrices = process(entree)
    print("go", len(matrices))

    #for i,m in enumerate(matrices):
    #    print (i)
    #debug(matrices)
    res1 = 0
    res2 = 0
    rows = 0
    cols = 0
    rows2 = 0
    cols2 = 0

    candidates = []
    for i, m in enumerate(matrices):
        if i == 97 :
            print("debug")

        mirrors = duplicate_adj(m)
        print("mirror ",i, mirrors)
        if len(mirrors['rows']) == 0 \
            and len(mirrors['cols']) == 0:
            print(i, 'no mirror ?? ')
        dump(m)

        for r in mirrors['rows']:
            rows += r
        for c in mirrors['cols']:
            cols += c
    res1 = 100 * rows + cols
    print("res1",res1, " = 100 * rows", rows,'+ cols', cols)

    candidates = []
    for i, m in enumerate(matrices):
        mir_smuged = duplicate_adj2(m)
        print("smuged ", i, mir_smuged)

        if len(mir_smuged['rows']) > 0:
            rows2 += mir_smuged['rows'][0]

        if len(mir_smuged['cols']) > 0:
            cols2 += mir_smuged['cols'][0]

    res2 = 100 * rows2 + cols2

    print("res1", res2, " = 100 * rows2", rows2, '+ cols2', cols2)
