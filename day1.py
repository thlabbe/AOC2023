import re

file = "./input1.txt"
# file = "./test1.txt"


def load():
    with open(file, "rt") as text:
        return text.readlines()


def part1():
    resp1 = 0
    for l in entree:
        numbers = re.findall(r"\d", l)

        tmp = int(numbers[0]) * 10 + int(numbers[-1])
        print(l, "->", numbers, tmp)
        resp1 += tmp
    return resp1


def part2():
    resp2 = 0
    spelled = {"one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "even": 7,
               "eight": 8,
               "nine": 9,
               "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }
    # rspelled = "("+ "|".join(spelled.keys()) + "?)"
    # rspelled = r"(one|two|three|four|five|six|even|eight|nine|1|2|3|4|5|6|7|8|9)"
    for l in entree:
        v1 = rech_gauche_droite(l, spelled)
        v2 = rech_droite_gauche(l, spelled)
        tmp = v1 * 10 + v2
        resp2 += tmp
    return resp2


def rech_gauche_droite(l, dic):
    res = []
    keys = dic.keys()
    for i in range(0, len(l), 1):
        for k in keys:
            if l[i:].startswith(k):
                res.append({"pos": i, "key": k, "value": dic.get(k)})

    return res[0].get("value")


def rech_droite_gauche(l, dic):
    res = []
    keys = dic.keys()
    for i in range(len(l), 0, -1):
        for k in keys:
            if l[:i].endswith(k):
                res.append({"pos": i, "key": k, "value": dic.get(k)})

    return res[0].get("value")


if __name__ == '__main__':
    entree = load()
    print(part1())
    print(part2())
