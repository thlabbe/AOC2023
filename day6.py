
FILE = "./input6.txt"
#FILE = "./test6.txt"

# brute force

def load():
    with open(FILE, "rt") as text:
        return text.read().splitlines()


def prepare(data):
    tmp = data[0].split(':')
    tmp2 = tmp[1].split(' ')
    times = []
    for t in tmp2:
        if len(t.strip()) > 0:
            times.append(int(t))

    tmp = data[1].split(':')
    tmp2 = tmp[1].split(' ')
    distances = []
    for d in tmp2:
        if len(d.strip()) > 0:
            distances.append(int(d))
    return times, distances

def prepare2(data):
    tmp = data[0].split(':')
    stime = tmp[1].split(' ')
    xxx = ''
    times = []
    for st in stime:
        if len(st.strip()) > 0:
            xxx = xxx + st
    times.append(int(xxx))

    tmp = data[1].split(':')
    sdist = tmp[1].split(' ')
    xxx = ''

    distances = []
    for sd in sdist:
        if len(sd.strip()) > 0:
            xxx = xxx + sd
    distances.append(int(xxx))
    return times, distances

def part1(times, distances):
    res = 1
    for i,t in enumerate(times):
        race = (t, distances[i])

        ways = count(race)
        res = res * ways
    print ("res = " ,res)

def count(race):

    t = race[0]
    d = race[1]
    c = 0
    for hold in range(1,t):
        if hold * (t - hold) > d :
            c += 1
    return c
def part2():
    pass

if __name__ == '__main__':
    data = load()
    times, distances = prepare(data)
    time, dist = prepare2(data)
    part1(times, distances)
    print("------")
    part1(time, dist)
    print("------")


