from functools import lru_cache

FILE = "./input12.txt"
FILE = "./test12.txt"


def load():

    with open(FILE, "rt") as text:
        return text.read().splitlines()

def process(data):
    infos = []
    for l in data:
        t = l.split(' ')
        s = t[0]
        r = list(map( int, t[1].split(',')))
        infos.append((s,r))
    return infos

DicoV = {}
def vector(s):
    if s in DicoV.keys():
        return DicoV[s]

    v = []
    t = s.split('.')
    ok = True
    for r in t:
        if len(r) > 0:
            if '?' in r:
                ok = False
            if ok:
                v.append(len(r))
    DicoV[s] = v
    return v


def valid_to_rank(v, crit):
    rank = len(v)
    return (v[:rank] == crit[:rank])


def valid(s, crit):
    t = s.split('.')
    v = []
    for r in t:
        if len(r) > 0:
            v.append(len(r))

    if (len(v)) == len(crit):
        return v == crit
    else: return False


def poss(s:str, crit):
    if s in Dico.keys():
        return Dico[s]

    if '?' not in s:
        Dico[s] = 1
        return 1
    else:
        liste = []
        pos = s.index('?')
        s1 = s[:pos] + '.' + s[pos + 1:]
        s2 = s[:pos] + '#' + s[pos + 1:]
        v1 = vector(s1)
        r1 = 0
        if valid_to_rank(v1, crit):
            r1 = poss(s1, crit)

            # if len(r1)> 0:
            #     if (len(r1[0]) == 1):
            #
            #         if valid(r1, crit):
            #             liste.append(r1)
            #     else:
            #         for row in r1:
            #
            #             if valid(row, crit):
            #                liste.append(row)
        r2 = 0
        v2 = vector(s2)
        if valid_to_rank(v2, crit):
            r2 = poss(s2, crit)
            # if len(r2) > 0:
            #    if (len(r2[0]) == 1):
            #        v2 = vector(r2)
            #        if valid(r2, crit):
            #            liste.append(r2)
            #    else:
            #        for row in r2:
            #
            #            if valid(row, crit):
            #                liste.append(row)
        Dico[s] = r1 + r2
        print( s, Dico[s],  r1 , '+', r2 )
        return Dico[s]




if __name__ == '__main__':

    data = load()
    infos = process(data)
    cnt1 = 0
    part2 = False
    for j, i in enumerate(infos):
        print( j , i)
        Dico = {}
        if not part2:
            crit = i[1]
            prop = i[0]
            test = poss(prop, crit)
            print(j, prop, crit, test)
        else:
            crit = i[1]  * 5
            prop = i[0]
            prop = '?'.join([prop,prop,prop,prop,prop,])
            test = poss(prop * 5, crit)
            print(j, prop, crit, test)

        cnt1 += test


    print(cnt1)
