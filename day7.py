FILE = "./input7.txt"
#FILE = "./test7.txt"

LABELS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
LABELS_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def is_five_of_a_kind(hand):
    """
Five of a kind, where all five cards have the same label: AAAAA
"""
    return (len(hand['count'].keys()) == 1)


def is_four_of_a_kind(hand):
    """
    Four of a kind, where four cards have the same label
    and one card has a different label: AA8AA
    """
    cnt = hand['count']
    ks = cnt.keys()
    vs = cnt.values()

    return (len(ks) == 2  # 2 cartes différentes
            and (4 in vs))  # la premiere y est 1 ou 4 fois ( pas 2 ou 3 )


def is_full_house(hand):
    """
    Full house, where three cards have the same label,
    and the remaining two cards share a different label: 23332
    """
    cnt = hand['count']
    ks = cnt.keys()
    if len(ks) == 2:
        vs = cnt.values()
        return 3 in vs
    return False


def is_three_of_a_kind(hand):
    """!
    Three of a kind, where three cards have the same label,
    and the remaining two cards are each different from any other card in the hand: TTT98
    """
    cnt = hand['count']
    ks = cnt.keys()
    vs = cnt.values()
    return (len(ks) == 3
            and 3 in vs)


def is_two_pair(hand):
    """
    Two pair, where two cards share one label,
    two other cards share a second label,
    and the remaining card has a third label: 23432
    """
    cnt = hand['count']
    ks = cnt.keys()
    vs = cnt.values()
    if ((len(ks) == 3)
            and 2 in vs
            and 1 in vs):
        # TODO : verifier qu'il y a 2 2 et 1 seul 1 dans vs
        return True
    return False


def is_one_pair(hand):
    """
    One pair, where two cards share one label,
    and the other three cards have a different label
    from the pair and each other: A23A4
    """
    cnt = hand['count']
    ks = cnt.keys()
    vs = cnt.values()
    return (len(ks) == 4)


def is_high(hand):
    """
    High card, where all cards' labels are distinct: 23456
    """
    return len(hand['count'].keys()) == 5


def substitue_j(s, l=[]):
    for idx, c in enumerate(s):
        if c == 'J':
            for x in LABELS_2[0:-1]:
                ns = s[:idx] + x + s[idx + 1:]
                l.append(ns)
                if 'J' in ns:
                    substitue_j(ns, l)

    return l


def hand_score2(hand):
    if 'J' not in hand['count'].keys():
        return hand_score(hand)
    alters = substitue_j(hand['hand'])
    score = 0
    for alt in alters:
        if score == 7:
            return score
        else:
            ht = hand
            ht['hand'] = alt
            ht['count'] = card_count(alt)

            score = max(score, hand_score(ht))

    return score


def hand_score(hand):
    s = 0
    if is_five_of_a_kind(hand):
        s = 7
    elif is_four_of_a_kind(hand):
        s = 6
    elif is_full_house(hand):
        s = 5
    elif is_three_of_a_kind(hand):
        s = 4
    elif is_two_pair(hand):
        s = 3
    elif is_one_pair(hand):
        s = 2
    else:  # High card
        s = 1
    return s



def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def hand_points2(hand):
    s = hand['hand']
    points = 0

    for i in range(5):  # range( card_rank('2'), card_rank('A'), -1):
        points = len(LABELS_2) * points + (len(LABELS_2) - card_rank(s[i]))

    return points


def hand_points(hand):
    s = hand['hand']
    points = 0
    for i in range(len(hand)):
        points = len(LABELS) * points + (len(LABELS) - card_rank(s[i]))

    return points


def prepare2(data):
    hands = []
    for idx, l in enumerate(data):
        print("prepare2", idx, l)
        t = l.split()
        hand = dict()
        hand['hand'] = t[0]
        hand['count'] = card_count(t[0])
        hand['bid'] = int(t[1])
        hand['index'] = idx
        hand['points'] = hand_points2(hand)
        hand['score'] = hand_score2(hand)
        hands.append(hand)

    return hands


def prepare1(data):
    hands = []
    for idx, l in enumerate(data):
        t = l.split()
        hand = dict()
        hand['hand'] = t[0]
        hand['count'] = card_count(t[0])
        hand['bid'] = int(t[1])
        hand['index'] = idx
        hand['points'] = hand_points(hand)
        hand['score'] = hand_score(hand)
        hands.append(hand)

    return hands


def card_rank(c):
    return LABELS.index(c)


def card_count(hand):
    counts = {}
    res = {}

    for v in LABELS:
        counts[v] = 0
    for c in hand:
        counts[c] += 1
    for k, v in counts.items():
        if v > 0:
            res[k] = v
    return res


def part2(data):
    hands = prepare2(data)
    print(" === ")
    first_order = {}
    for x in range(8):
        first_order[x] = []

    for idx, h in enumerate(hands):
        first_order[h['score']].append(h)
    rank = 1
    for k, v in first_order.items():
        new_list = sorted(v, key=lambda x: x['points'])

        for nh in new_list:
            nh['rank'] = rank
            rank += 1
            hands[nh['index']] = nh

            xxx = (nh['bid'] * nh['rank'])

    res = 0
    for idx,h in enumerate(hands):
        xxx = (h['bid'] * h['rank'])
        print(idx)
        res += xxx
    print("res = ", res)


def part1(data):
    hands = prepare1(data)
    first_order = {}
    for x in range(8):
        first_order[x] = []

    for idx, h in enumerate(hands):
        first_order[h['score']].append(h)
    rank = 1
    for k, v in first_order.items():
        new_list = sorted(v, key=lambda x: x['points'])

        for nh in new_list:
            nh['rank'] = rank
            rank += 1
            hands[nh['index']] = nh

    res = 0
    for idx, h in enumerate(hands):
        xxx = (h['bid'] * h['rank'])
        print(idx)
        res += xxx
    print("res = ", res)


if __name__ == '__main__':
    data = load()
    part1(data)
    print("------")
    part2(data)
    print("++++")