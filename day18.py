from collections import defaultdict, deque
FILE = 'input18.txt'
#FILE = 'test18.txt'

DIRS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
DIRS2 = {'0': (0, 1), '1': (1, 0), '2': (0, -1), '3': (-1, 0)}
def load():
    with open(FILE) as f:
        return f.read().strip().split('\n')
def parse1(lst):
    res = []
    for line in lst:
        line = line.strip().split(" ")
        dir = DIRS[line[0]]
        len = int(line[1])
        res.append((dir, len))
    return res

def parse2(lst):
    res = []
    for line in lst:
        hexa = line.strip().split()[2][2:-1]
        len = int(hexa[0:5], 16)
        dir = DIRS2[hexa[5]]
        res.append((dir, len))
    return res

def addAndMultiply(t1: tuple, t2:tuple, mult:int):
    return (t1[0] + t2[0] * mult, t1[1] + t2[1] * mult)

def points(plan):
    start = (0, 0)
    coords = [start]
    prevPos = start
    perim = 1
    for (dir, len) in plan:
        nextPos = addAndMultiply(prevPos, dir, len)
        perim += len
        coords.append(nextPos)
        prevPos = nextPos
    return perim, coords

def area(perim, coords):
    res = 0

    # Shoelace / Lacets # Formule de Gauss pour obtenir
    # l'aire d'un polygone à partir des coordonnées des sommets
    for i in range(1, len(coords)):
        x1, y1 = coords[i -1]
        x2, y2 = coords[i]
        res += (y1 + y2) * (x1 - x2)
    return (abs(res) + perim + 1) / 2

liste = load()
plan = parse1(liste)
perim, coords = points(plan)
res1 = area(perim, coords)
print(f"part1 : {res1}")

plan2 = parse2(liste)
perim2, coords2 = points(plan2)
res2 = area(perim2,coords2)
print(f"part2 : {res2}")
