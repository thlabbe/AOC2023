FILE = "./input10.txt"
FILE_TEST = "./test10.txt"
#FILE = FILE_TEST
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
DIRECTIONS = { 'N': (  0, -1 ),
               'S' :(  0, +1 ),
               'E' :( +1,  0 ),
               'W' :( -1,  0 ),}

def load():

    with open(FILE, "rt") as text:
        return text.read().splitlines()


def start_and_grid(data):
    grid = []
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        grid.append(data[y])


    start = None
    for y in range(rows):
        for x in range(cols):
            if read_at(x, y, grid) == 'S':
                start = (x, y)
    print(start)
    print(" ! " ,read_at(start[0], start[1], grid))
    # FIXME : bof bof bof
    if FILE_TEST == FILE:
        subst = 'F'
    else:
        subst = 'J'

    grid = set_at(subst, start[0], start[1], grid)
    print(" - " ,read_at(start[0], start[1], grid))
    return start, grid
def read_at(x, y, table):
    row = table[y]
    car = row[x]
    return car

def set_at(value, x, y, table):
    s = table[y]
    table[y] = s[:x] + value + s[x+1:]
    return table

CONNECTIONS = { '|' : ('N', 'S'),
                '-' : ('W', 'E'),
                'L' : ('N', 'E'),
                'J' : ('N', 'W'),
                '7' : ('S', 'W'),
                'F' : ('S', 'E'),
                '.' : (None, None)
                }
"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this
"""



def part1(start, grid):
    dir = 'S' # on part vers le SOUTH ( ok pour tests et input )
    path = []
    pos = start
    if FILE_TEST == FILE:
        dir = 'S'
    else:
        dir = 'N'

    while not (pos == start and len(path) > 1):
        path.append(pos)

        move = DIRECTIONS[dir]

        new_pos = (pos[0] + move[0], pos[1] + move[1])
        print(pos, dir, move, new_pos)
        new_dir = 'X'
        tile = read_at(new_pos[0], new_pos[1], grid)

        if tile == '.' :
            print('ERREUR : ', tile, dir )
            new_dir = ''
        elif tile in '|-' :
            new_dir = dir
        elif tile == 'L':
            if dir == 'S': new_dir = 'E'
            elif dir == 'W': new_dir = 'N'
            else : print('ERREUR : ', tile, dir )
        elif tile == 'J':
            if dir == 'S': new_dir = 'W'
            elif dir == 'E' : new_dir = 'N'
            else: print('ERREUR : ', tile, dir )
        elif tile == '7':
            if dir == 'N': new_dir = 'W'
            elif dir == 'E' : new_dir = 'S'
            else: print('ERREUR : ', tile, dir )
        elif tile == 'F':
            if dir == 'N': new_dir = 'E'
            elif dir == 'W' : new_dir = 'S'
            else: print('ERREUR : ', tile, dir )
        # print(f"position {pos} {read_at(pos[0], pos[1], grid)}  direction {dir} -> {new_pos} {new_dir} : {tile} ")
        pos = new_pos
        dir = new_dir

    # print(path)
    # print(len(path))
    print(len(path) /2)
    return path

def clean(grid,path):
    new_grid = []
    interior = []
    exterior = []
    for y in range(len(grid)):
        last_tile = ''
        nb_bords = 0
        for x in range(len(grid[0])):
            if (x, y) in path:
                curr_tile = read_at(x, y, grid)
                if curr_tile == '|':
                    nb_bords += 1
                elif curr_tile == '7' and last_tile =='L':
                    nb_bords +=1
                elif curr_tile == 'J' and last_tile =='F':
                    nb_bords +=1

                if curr_tile != '-':
                    last_tile = curr_tile
            else:
                if nb_bords % 2 == 1:
                    interior.append((x,y))
                else:
                    exterior.append((x,y))

    for y in range(len(grid)):
        row = ''
        for x in range(len(grid[0])):
            c = 'x'
            if (x,y) in path:
                c = '.'
            elif (x,y) in interior: c = 'I'
            elif (x,y) in exterior: c = 'O'
            else: c = ' '
            row = row + c
        new_grid.append(row)

    for i in range(len(new_grid)):
        print ('[', new_grid[i], ']')

    print(len(interior))


    return new_grid

if __name__ == '__main__':

    data = load()
    start , grid = start_and_grid(data)
    path = part1(start, grid)

    new_grid = clean(grid, path)

    # print("part1 : ", part1())
    # print("part2 : ", part2())
