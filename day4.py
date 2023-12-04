file = "./input4.txt"
#file = "./test4.txt"


def load():

    with open(file, "rt") as text:
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

        liste.append( {'id':number,
                       'winning': win_nums,
                       'hand': plays_nums})
    return liste
def part2():
    return 0

def part1():
    data = load()
    games = preprocess(data)
    #{'id':number, 'winning': win_nums, 'hand': plays_nums}
    total = 0
    for g in games:
        count = 0
        win_num = g['winning']
        hand = g['hand']
        for w in win_num:
            if w in hand:
                count += 1
        if count > 0:
            total += 2 ** (count - 1)

    return total



if __name__ == '__main__':

    print("part1 : ",part1())
    print("part2 : ", part2())

