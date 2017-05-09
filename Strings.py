def camelCase():
    s = input()
    count = 0
    for c in s:
        if (c < 'a'):
            count += 1
    print(count + 1)


def twoCharacters():
    _ = input()
    s = input()
    k = 0
    chars = set(s)  # distinct chars
    import itertools
    for combs in itertools.combinations(chars, 2):
        ns = s
        nset = chars - set(combs)
        for c in nset:#chars - set(combs):
            ns = str.replace(ns, c, '')
        if twoCharCheck(ns):
            # print(ns, k,nset)
            k = max(k,len(ns))
    print(k)


def twoCharCheck(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def marsExploration():
    s = input()
    sos = 'SOS'*(len(s)//3)
    count = [1 if a != b else 0 for a, b in zip(s,sos)]
    print(sum(count))

marsExploration()
