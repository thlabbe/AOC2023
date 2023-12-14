
FILE = "./input11.txt"
FILE = "./test11.txt"

# brute force

def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def to_grid(data):
    res = []
    rows = len(data)

    for y in range(rows):
        res.append(data[y])

    return res

def rotate(grid):
    print(grid)
    arr = list(zip(*grid[::-1]))
    res = []
    for y in arr:
        res.append(''.join(y))
    return res

def expand(grid):

    rows = len(grid)
    row_exp = []
    for y in range(rows):
        slice = grid[y]
        if slice == '.' * len(slice):
            row_exp.append(y)
            #res.append(slice)

    return row_exp

def galaxies(grid):
    res = []
    rows = len(grid)
    cols = len(grid[0])

    for y in range(rows):
        for x in range(cols):
            if read_at(x, y, grid) == '#':
                res.append((x,y))
    return res
def read_at(x, y, table):
    row = table[y]
    car = row[x]
    return car

def set_at(value, x, y, table):
    s = table[y]
    table[y] = s[:x] + value + s[x+1:]
    return table

def distance(p1, p2):
    """mannathan distance"""
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def distance_2(p1, p2, rows, cols, factor):
    """mannathan distance"""
    d1 = distance(p1, p2)
    d = d1
    for x in range(p1[0], p2[0]):
        if x in cols :
            d += factor - 1
            print(x, 'cols :', p1,p2, cols, rows )
    for y in range(p1[1], p2[1]):
        if y in rows :
            d += factor - 1
            print(y, 'rows :', p1, p2, cols, rows)
    print(d1, d)
    return d


if __name__ == '__main__':
    row_exp = []
    data = load()
    grid = to_grid(data)
    row_exp = expand(grid)

    rot = rotate(grid)

    col_exp = []
    col_exp = expand(rot)

    grid = rotate(rotate(rotate(rot)))

    d_galaxies = {}
    glx = galaxies(grid)
    for i, g in enumerate(glx):
        d_galaxies[i+1] = g
        print(i,g)
    dist = {} # distance between 2 galaxies
    # part1
    # for start in d_galaxies.keys():
    #     for to in d_galaxies.keys():
    #         if (f"{start} {to}" not in dist.keys()) \
    #                 and (f"{to} {start}" not in dist.keys()):
    #             dist[f"{start} {to}"] = distance(d_galaxies[start], d_galaxies[to])
    # res = 0

    for r in grid:
        print(r)
    print(row_exp, col_exp)
    # part2
    res = 0
    for k,v in dist.items():
        res += v
    for start in d_galaxies.keys():
        for to in d_galaxies.keys():
            if (f"{start} {to}" not in dist.keys()) \
                    and (f"{to} {start}" not in dist.keys()):
                dist[f"{start} {to}"] = distance_2(d_galaxies[start], d_galaxies[to], row_exp, col_exp, 1)
    res = 0
    for k,v in dist.items():
        res += v

    print(res)
