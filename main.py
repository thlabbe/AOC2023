import re

file = "./input2.txt"
# file = "./test2.txt"

EMPTY_HAND = {'green': 0, 'red': 0, 'blue': 0}


def load():

    with open(file, "rt") as text:
        return text.read().splitlines()


def part1():
    question = { "red" : 12 , 'green' : 13, 'blue' : 14}
    games = []
    for ligne in entree:
        hs = []
        t1 = ligne.split(':')
        # id = int(t1[0].split(' ')[1])
        hands = t1[1].split(';')
        for h in hands:
            hs.append(trait_hand(h))

        games.append(hs)

    total = 0
    for idx, g in enumerate(games):
        if valid_game(g, question) :
            total += idx + 1

    total2 = 0
    minimas = []
    for idx, g in enumerate(games):
        mini_g = minimize_game(g)
        minimas.append(mini_g)
        power = mini_g['green'] * mini_g['blue'] * mini_g['red']

        total2 += power

    return total, total2


def trait_hand(s):
    res = dict()
    res['blue'] = 0
    res['green'] = 0
    res['red'] = 0
    colors = s.split(',')

    for c in colors:
        x = c.strip().split(' ')
        # print(c, "->", x)
        val = int(x[0])
        key = x[1]
        res[key] = val

    return res


def valid_game(game, question):
    valid = True
    for hand in game:
        for k, v in hand.items():
            valid = valid and question[k] >= v

    return valid


def minimize_game(game):
    x = {'red' : 0, 'green' : 0, 'blue' : 0}
    for hand in game:
        for k, v in hand.items():
            if v > 0 and x[k] < v :
                x[k] = v

    return x


if __name__ == '__main__':
    entree = load()
    print(part1())

