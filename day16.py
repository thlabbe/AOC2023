import sys
sys.setrecursionlimit(10000)

FILE = "./input16.txt"
# FILE = "./test16.txt"

DIRECTIONS = { 'UP': (  0, -1 ),
               'DOWN' :(  0, +1 ),
               'LEFT' :( -1,  0 ),
               'RIGHT' :( +1,  0 ),}


def read_at(pos, table):
    row = table[pos[1]]
    value = row[pos[0]]
    return value

def set_at(value, pos, table):
    s = table[pos[1]]
    # print(f"{pos} [{s[:pos[0]]}+ {value} + {s[pos[0] + 1:]}]")
    row = s[:pos[0]]
    row.append(value)
    for i in s[pos[0]+1:]:
        row.append(i)

    table[pos[1]] = row
    return table


def load():
    mat = []
    with open(FILE, "rt") as text:
        for r in text.read().splitlines():
            mat.append(tuple([c for c in r]))
    max_row = len(mat)
    max_col = len(mat[0])
    return tuple(mat), (max_col, max_row)

def find_mirrors(table):
    res = {}

    rows = len(table)
    cols = len(table[0])
    for r in range(rows):
        for c in range(cols):
            pos = (c,r)
            car = read_at(pos, table)
            if car != '.':
                res[pos] = car

    return res

def dump_mat(it, msg):
    print(msg)
    for i,x in enumerate(it):
        print(f"{i}\t{' '.join(x)}")
def dump(energized, maxis, msg=""):

    max_col, max_row = maxis
    mat = []
    row = []
    for c in range(max_col):
        row.append('.')

    for r in range(max_row):
        mat.append( row )
    for k,v in energized.items():
        for pos in v:
            mat = set_at('#', pos, mat)
    dump_mat(mat, msg)
def pos_in_range(pos, maxis):
    res =  pos[0] >= 0 and pos[1] >= 0 and pos[0] < maxis[0] and pos[1] < maxis[1]
    #if not res :
    #    print("*** out : ", pos, maxis )
    return res

def bouncing(beam, mir):
    pos = beam['pos']
    dir = beam['dir']
    if mir == "/":
        if dir == 'UP':
            dir_label = 'RIGHT'
        elif dir == 'DOWN':
            dir_label = 'LEFT'
        elif dir == 'LEFT':
            dir_label = 'DOWN'
        elif dir == 'RIGHT':
            dir_label = 'UP'
    else: # mir == '\'
        if dir == 'UP':
            dir_label = 'LEFT'
        elif dir == 'DOWN':
            dir_label = 'RIGHT'
        elif dir == 'LEFT':
            dir_label = 'UP'
        elif dir == 'RIGHT':
            dir_label = 'DOWN'
    ndir = DIRECTIONS[dir_label]
    return (pos[0] + ndir[0], pos[1] + ndir[1]), dir_label

def spliting(beam, mir):
    pos = beam['pos']
    dir = beam['dir']
    if mir == "|" and dir in ['LEFT', 'RIGHT']:
        dir_label1 = 'UP'
        dir_label2 = 'DOWN'

    else: # mir = '-' and dir in ['UP', 'DOWN']:
        dir_label1 = 'LEFT'
        dir_label2 = 'RIGHT'

    ndir1 = DIRECTIONS[dir_label1]
    ndir2 = DIRECTIONS[dir_label2]

    return ((pos[0] + ndir1[0], pos[1] + ndir1[1]),
            dir_label1,
            (pos[0] + ndir2[0], pos[1] + ndir2[1]),
            dir_label2)


def fusion(e1, e2):
    en = {}
    for k1,v1 in e1.items():
        for k2, v2 in e2.items():
          if k1 == k2:
              en[k1] = v1 + v2
    return en

def score(e):
    lst = []
    for k,v in e.items():
        for p in v:
            lst.append(p)
    lst = list(set(lst))
    return len(lst)

def walk(beam, mirrors, energized, maxis, cnt):

    if beam is None:
        return energized
    pos = beam['pos']
    dir = beam['dir']
    if not pos_in_range(pos, maxis):
        return energized

    if pos in energized[dir]: # prevent loop
        return energized

    energized[dir].append(pos)

    next_pos1 = None
    next_pos2 = None

    if pos not in mirrors.keys(): # pas de mirroir on continue dans la meme direction
        next_pos1 = ( pos[0] + DIRECTIONS[dir][0] , pos[1] + DIRECTIONS[dir][1])
        dir1 = dir
    else:
        mir = mirrors[pos]
        if (mir == '-' and (dir == 'LEFT' or dir == 'RIGHT')) \
               or ( mir == '|' and (dir == 'UP' or dir == 'DOWN')):
            next_pos1 = (pos[0] + DIRECTIONS[dir][0], pos[1] + DIRECTIONS[dir][1])
            dir1 = dir
        elif (mir in '\\/'):
            next_pos1, dir1 = bouncing(beam, mir)
        else:
            #print("split")
            next_pos1, dir1, next_pos2, dir2 = spliting(beam, mir)
    if next_pos1 is None:
        print("*** ERREUR ", beam, next_pos1, next_pos2)
    if next_pos2 is None:
        return  walk({'pos' : next_pos1, "dir": dir1}, mirrors, energized, maxis,cnt)
    else:

        e1 = walk({'pos' : next_pos1, "dir": dir1}, mirrors, energized, maxis, cnt)
        e2 = walk({'pos' : next_pos2, "dir": dir2}, mirrors, energized, maxis, cnt)
        return fusion(e1 , e2)

def part1(mirrors, maxis):
    energized = { 'UP' :[],
                  'DOWN' : [],
                  'LEFT' : [],
                  'RIGHT' : []}

    start = {'pos' : (0,0), 'dir': 'RIGHT'}
    beam = start
    res = score(walk(beam, mirrors, energized, maxis, 1))
    print(res)

def part2(mirrors, maxis):
    s = 0
    for i in range(maxis[0]):
        energized = {'UP': [],
                     'DOWN': [],
                     'LEFT': [],
                     'RIGHT': []}
        beam = {'pos': (i, maxis[1]), 'dir': 'UP'}
        s = max(s, score(walk(beam, mirrors, energized, maxis, 0)))
        print(" tmp ", s)
        energized = {'UP': [],
                     'DOWN': [],
                     'LEFT': [],
                     'RIGHT': []}
        beam = {'pos' : (i,0), 'dir': 'DOWN'}
        s = max(s, score(walk(beam, mirrors, energized, maxis, 0)))
        print(" tmp ", s)

    for i in range(maxis[1]):
        energized = {'UP': [],
                     'DOWN': [],
                     'LEFT': [],
                     'RIGHT': []}
        beam = {'pos': (0, i), 'dir': 'RIGHT'}
        s = max(s, score(walk(beam, mirrors, energized, maxis, 0)))
        print(" tmp ", s)
        energized = {'UP': [],
                     'DOWN': [],
                     'LEFT': [],
                     'RIGHT': []}
        beam = {'pos': (maxis[0], i), 'dir': 'LEFT'}
        s = max(s, score(walk(beam, mirrors, energized, maxis, 0)))
        print(" tmp ", s)
    print("part2 :", s)

if __name__ == '__main__':

    mat, maxis = load()
    #dump_mat(mat,'start')
    mirrors= find_mirrors(mat)
    print(len(mirrors),'mirroirs')
    #part1(mirrors, maxis)
    #dump_mat(mat, 'start')
    part2(mirrors, maxis)


