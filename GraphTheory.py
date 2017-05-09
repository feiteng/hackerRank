import collections


def bfsShortReach():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        d = collections.defaultdict(set)
        # for i in range(1,n+1):
        #     d[i]=set()
        dist = collections.defaultdict()
        for ops in range(m):
            u, v = map(int, input().split())
            d[u].add(v)
            d[v].add(u)
        s = int(input())
        q = [s]
        length = 0
        while q:
            tmpq = []
            while q:
                next = q.pop()
                if next in dist:
                    continue
                dist[next] = length
                [tmpq.append(n) for n in d[next]]
            length += 6
            q = tmpq
        plist = []
        for i in range(1, n + 1):
            if i == s:
                continue
            if i in dist:
                plist.append(dist[i])
            else:
                plist.append(-1)
        print(' '.join(map(str, plist)))


import collections


def roadsAndLibraries():
    for _ in range(int(input())):
        n, m, clib, croad = map(int, input().split())
        d = collections.defaultdict(set)
        for i in range(1, n + 1):
            d[i] = set()
        for k in range(m):
            u, v = map(int, input().split())
            d[u].add(v)
            d[v].add(u)
        cost = 0
        s = set()
        for k in d.keys():
            num = findNeighbour(k, d, s)
            if num > 0:
                if num == 1:
                    cost += clib
                else:
                    cost += min((num - 1) * croad + clib, num * clib)
        print(cost)


import collections


def findNeighbour(k, d, keySet):
    if k in keySet:
        return 0
    l = [k]
    s = set()
    while l:
        ltmp = []
        while l:
            next = l.pop()
            if next in s:
                continue
            s.add(next)
            [ltmp.append(n) for n in d[next]]
        l = ltmp
    [keySet.add(n) for n in s]
    return len(s)


def journeyToTheMoon():
    n, p = map(int, input().split())
    d = collections.defaultdict(set)
    for i in range(n):
        d[i] = set()
    for _ in range(p):
        u, v = map(int, input().split())
        d[u].add(v)
        d[v].add(u)
    groups = []
    s = set()
    for k in d.keys():
        num = findNeighbour(k, d, s)
        if num > 0:
            groups.append(num)
    comb = 0
    sum = 0
    result = 0
    for size in groups:
        result += sum * size
        sum += size
    print(result)


journeyToTheMoon()
