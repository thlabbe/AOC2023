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


def max_max(maps):
    res = -1
    for map in maps:
        for x,y,z in map['ranges']:
            res = max(res,x + z)
            res = max(res, y + z)
    return res


def hash_ranges(ranges, map):
    """ Renvoyer la liste des ranges
    ordonnée qui en y appliquant la map donnera des résultats croissants.

    expl :
        ranges :
            [(0,100]]
        map :
            50 98 2
            52 50 48

    seed  soil
    0     0
    1     1
    ...   ...
    48    48
    49    49
    50    52
    51    53
    ...   ...
    96    98
    97    99
    98    50
    99    51

    =>
    invert = [  (0, 49),
                (98, 99),
                (50, 97) ]
    """
    print(ranges)
    new_ranges = []
    map_src = []
    map_dest = []

    for dest, src, width in map['ranges']:
        print('dest, src, width:',dest, src, width)
        map_src.append((src, src + width))
        map_dest.append(((dest, dest + width)))
    dic = dict()
    cid = dict()
    for i, src in enumerate(map_src):
        dic[map_src[i]] = map_dest[i]
        cid[map_dest[i]] = map_src[i]

    for k,v in dic.items():
        print('dic',k,'->' ,v)
    for k,v in cid.items():
        print('cid',k,'->',v)
    for i,r in enumerate(ranges):
        s = r[0]
        e = r[1]
        print(i, r, s, e )
        new_ranges = segment(r, cid)

    return new_ranges

def segment(r, map):
    print("+++",r, map)
    res = []
    min_, max_ = r[0], r[1]
    r_start = min_
    r_end = min_
    for k in map.keys():
        print(k)
        k_deb = k[0]
        k_fin = k[1]
        if k_deb > r_end:
            res.append((r_start,k_deb))
            r_start = k_deb + 1
        elif k_deb > r_start :
            if k_fin < r_start:
                res.append((k_deb, k_fin))
                r_start = k_fin +1
            else:
                res.append((k_deb, r_start))
                r_start = r_fin + 1
    res.append((r_start, max_ ))

    print("===", res)
    return res

def part2(seeds_ranges, maps):
    # TODO : MemoryError avec le puzzle :) ( 1^10 valeurs à traiter )
    max = max_max(maps)
    print("max", max ) # max = 4294967296 :D

    ranges1 = (0, max)
    ranges = [ranges1]
    ranges2 = hash_ranges(ranges, maps[0])
    print("***" , ranges2)
    res = max
    pairs =[]
    '''for b in range(0 ,len(seeds_ranges),2):
        pairs.append((seeds_ranges[b],seeds_ranges[b] + seeds_ranges[b+1]))
    pairs = unionize(pairs)
    brute = set()'''
    '''for p in pairs:
        l = [x for x in range(p[0], p[1])]
        for i in l:
            brute.add(i)

    for i in brute:
        res = min(res, transform(i,maps))'''
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
    # print("part2 : ", part2(seeds, maps)) # 46 OK
