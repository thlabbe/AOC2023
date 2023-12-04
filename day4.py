FILE = "./input4.txt"
# FILE = "./test4.txt"


def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def preprocess(data):
    liste = []
    for line in data:
        t1 = line.split(':')
        number = int(t1[0][4:])

        t2 = t1[1].split('|')
        win_nums = []
        for n in t2[0].split(' '):
            if n > '':
                win_nums.append(int(n))
        plays_nums = []
        for n in t2[1].split(' '):
            if n > '':
                plays_nums.append(int(n))

        liste.append({'id': number,
                      'winning': win_nums,
                      'hand': plays_nums,
                      'score': 0})
    return liste


def part2(scored): # : FIXME trop de bricolages sur les indices +/- 1
    res = 0
    scores = []
    for x in range(1 + len(scored)):
        scores.append(0)

    for x in range(1, len(scored)):
        scores[x] += 1
        g = scored[x - 1]
        s = scored[g['score']]

        for y in range(1 + x, x + s['id']):
            scores[y] += scores[x]

    for s in scores:
        res += s
    return res + 1 # FIXME : c'est moche


def part1():
    data = load()
    games = preprocess(data)
    # {'id':number, 'winning': win_nums, 'hand': plays_nums}
    total = 0
    scored = []
    for g in games:
        count = 0
        win_num = g['winning']
        hand = g['hand']
        for w in win_num:
            if w in hand:
                count += 1
        g['score'] = count
        scored.append(g)

        if count > 0:
            total += 2 ** (count - 1)

    return total, scored


if __name__ == '__main__':
    res1, data2 = part1()
    print("part1 : ", res1)
    print("part2 : ", part2(data2))
