import functools

FILE = "./input5.txt"
FILE = "./test5.txt"


def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def preprocess(data):
    seeds = []

    t0 = data[0].split(': ')
    # print(t0[1].split(' '))
    for st in t0[1].split(' '):
        seeds.append(int(st))

    maps = []
    lst = []
    for line in data[1:]:

        if line == '' and len(lst) > 0:
            my_map = make_map(lst)
            maps.append(my_map)
            lst = []
        elif line != '':
            lst.append(line)
    my_map = make_map(lst)
    maps.append(my_map)

    return seeds, maps


def make_map(table):
    res = dict()
    #print("make_map " + table[0])
    t0 = table[0].split(' ')
    name =  t0[0]
    res['name'] = name
    ranges = []
    for line   in table[1:]:
        t1 = line.split(' ')
        destination_range_start, source_range_start, the_range_length = int(t1[0]),  int(t1[1]),  int(t1[2])
        ranges.append((destination_range_start, source_range_start, the_range_length))

    res['ranges'] = ranges
    return res


def lookup(value, map:dict):
    res = value
    found = False
    for dest, src, width in map['ranges']:
        range_src = range(src, src + width)
        range_dest = range(dest, dest + width)
        found = value in range_src
        if found :
            idx = range_src.index(value)
            res = range_dest[idx]
    return res



def transform(seed, maps):
    # seed - to - soil
    soil = lookup(seed, maps[0])
    # soil - to - fertilizer
    fertilizer = lookup(soil, maps[1])
    # fertilizer - to - water
    water = lookup(fertilizer, maps[2])
    # water - to - light
    light = lookup(water, maps[3])
    # light - to - temperature
    temperature = lookup(light, maps[4])
    # temperature - to - humidity
    humidity = lookup(temperature, maps[5])
    # humidity-to-location
    location = lookup(humidity, maps[6])
    return location

def unionize(ranges):
    b = []
    for begin, end in sorted(ranges):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b

def part2(seeds_ranges, maps):
    # TODO : MemoryError avec le puzzle :) ( 1^10 valeurs à traiter )
    res = 999_999_999_999
    pairs =[]
    for b in range(0 ,len(seeds_ranges),2):
        pairs.append((seeds_ranges[b],seeds_ranges[b] + seeds_ranges[b+1]))
    pairs = unionize(pairs)
    brute = set()
    for p in pairs:
        l = [x for x in range(p[0], p[1])]
        for i in l:
            brute.add(i)

    for i in brute:
        res = min(res, transform(i,maps))
    return res


def part1(seeds, maps):
    res = 999999999999

    for seed in seeds:
        location = transform(seed, maps)
        res = min(res, location)

    return res


if __name__ == '__main__':

    data = load()


    maps = []
    seeds, maps = preprocess(data)
    # print(seeds, '\n ' , maps)
    print("part1 : ", part1(seeds, maps)) # 35 OK
    print("part2 : ", part2(seeds, maps)) # 46 OK
