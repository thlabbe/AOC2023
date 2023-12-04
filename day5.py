FILE = "./input5.txt"
FILE = "./test5.txt"


def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def preprocess(data):
    liste = []
    for line in data:


        liste.append(data)
    return liste


def part2():
    res = 0
    datas = preprocess(load())

    return res


def part1():
    res = 0
    datas = preprocess(load())

    return res


if __name__ == '__main__':

    print("part1 : ", part1())
    print("part2 : ", part2())
