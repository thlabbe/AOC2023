file = "./input3.txt"
# file = "./test3.txt"

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
DIRECTIONS = [ (-1, -1, 'NW'),(+1, -1, 'NE'),(+1, +1, 'SE'),(-1, +1, 'SW'),
               (-1, 0, 'N'),(+1, 0, 'S'),( 0, +1, 'E'),(0, -1, 'W'),]

def load():

    with open(file, "rt") as text:
        return text.read().splitlines()

def part2():
    data = load()
    schem = load_schematic(data)
    coords = star_pos(schem)
    sum = 0
    for x, y, c  in coords:
        nums = []
        for dx, dy, dir in DIRECTIONS:
            x1 = x + dx
            y1 = y + dy
            c1 = read_at(x1, y1, schem)
            if c1 in NUMBERS:
                n = ''

                x2 = x1
                while read_at(x2, y1, schem) in NUMBERS:
                    x2 += 1

                x2 -= 1
                while read_at(x2, y1, schem) in NUMBERS:
                    n = read_at(x2, y1, schem) + n
                    schem = set_at('.', x2, y1, schem)
                    x2 -= 1
                nums.append(int(n))
        if len(nums) == 2:
            sum += nums[0] * nums[1]

    return sum

def part1():
    data = load()
    schem = load_schematic(data)
    coords = symbol_pos(schem)

    nums = []
    for x, y, c  in coords:
        for dx, dy, dir in DIRECTIONS:
            x1 = x + dx
            y1 = y + dy
            c1 = read_at(x1, y1, schem)
            if c1 in NUMBERS:

                n = ''

                x2 = x1
                while read_at(x2, y1, schem) in NUMBERS:
                    x2 += 1

                x2 -= 1
                while read_at(x2, y1, schem) in NUMBERS:
                    n = read_at(x2, y1, schem) + n
                    schem = set_at('.', x2, y1, schem)
                    x2 -= 1

                nums.append(int(n))
    res= 0
    for n in nums:
        res += n
    return res


def load_schematic(data):
    schematic = []
    a_dot_row = '.' * len (data[0]) + '.'
    schematic.append(a_dot_row)
    for line in data:
        schematic.append('.' + line + '.')
    schematic.append(a_dot_row)

    return schematic

def symbol_pos(table):
    coords = []
    rows = len(table)
    cols = len(table[0])
    for y in range(rows):
        row = table[y]
        for x in range(cols):
            car = row[x]
            if car not in NUMBERS and car != '.':
                coords.append((x,y,car))

    return coords

def star_pos(table):
    res = []
    for x,y,car in symbol_pos(table):
        if car == '*' :
            res.append((x,y,car))
    return res


def read_at(x, y, table):
    row = table[y]
    car = row[x]
    return car


def set_at(value, x,y, table):
    s = table[y]
    table[y] = s[:x] + value + s[x+1:]
    return table

if __name__ == '__main__':

    print("part1 : ",part1())
    print("part2 : ", part2())

