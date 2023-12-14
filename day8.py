FILE = "./input8.txt"
# FILE = "./test8.txt"
# FILE = "./test8b.txt"

def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def prep(data):
    path = []
    for c in data[0]:
        path.append(c)

    nodes = {}
    # |GLJ = (QQV, JTL)|
    # |0123456789012345
    for line in data[2:]:
        key = line[0:3]
        left = line[7:10]
        right =line[12:15]
        nodes[key] = {'L': left, 'R': right}
    return path, nodes

def part1(path, nodes):
    step = 0
    key = 'AAA'
    res = solve_ZZZ(key, path, nodes,step)
    print(res)

def solve_ZZZ(key, path, nodes, step=0 ):
    res = step
    while key[2] != 'ZZZ':
        if step == len(path):
            # print("*** loop")
            step = 0

        side = path[step]
        step += 1
        res += 1
        key = nodes[key][side]
    return res

def solve_xxZ(key, path, nodes, step=0 ):
    res = step

    while key[2] != 'Z':
        step = ( step % len(path) )#if step == len(path):
        # print("*** loop")
        #    step = 0
        # print(step, len(path))
        side = path[step]
        step += 1
        res += 1
        key = nodes[key][side]
    return res

def test_keys_ends_with_Z(keys):
    res = True
    for k in keys:
        res = res and k[2] == 'Z'
    if res : print(' test ok ' ,keys)
    return res

def next(key, side, nodes):
    return nodes[key][side]

def part21(path, nodes):
    step = 0
    keys = []
    for k in nodes.keys():
        if k[2] == 'A':
            keys.append(k)
    print('start : ', keys)
    for idx,k in enumerate(keys):
        res = solve_xxZ(k, path, nodes,step)
        step = res
        print(idx,k)

def part2(path, nodes):
    step = 0
    keys = []
    for k in nodes.keys():
        if k[2] == 'A':
            keys.append(k)
    print('start : ', keys)

    res = step
    while not(test_keys_ends_with_Z(keys) ): # key != 'ZZZ':
        side = path[step]
        step += 1
        res += 1
        if (res % 1_000_000_000) == 0: print(res, '...')
        if step == len(path):
            # print("*** loop")
            step = 0
        next_keys = []
        for key in keys:
            next_keys.append(next(key,side,nodes))
        keys = next_keys
    print(res)

if __name__ == '__main__':
    data = load()
    path, nodes = prep(data)
    # part1(path, nodes)
    print(len(path), path)
    part21(path, nodes)