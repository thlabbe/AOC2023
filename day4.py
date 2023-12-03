file = "./input4.txt"
# file = "./test4.txt"

def load():

    with open(file, "rt") as text:
        return text.read().splitlines()

def part2():
    return 0

def part1():
    data = load()
    return 0



if __name__ == '__main__':

    print("part1 : ",part1())
    print("part2 : ", part2())

