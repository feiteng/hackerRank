def findTheBug():
    list = [input() for _ in range(int(input()))]
    for i in range(len(list)):
        if 'X' in list[i]:
            print('{},{}'.format(i, list[i].index('X')))
            return


def comparingTime():
    import time
    for _ in range(int(input())):
        time1, time2 = input().split(' ')
        t1 = time.strptime(time1, '%I:%M%p')
        t2 = time.strptime(time2, '%I:%M%p')
        if t1 < t2:
            print('First')
        else:
            print('Second')


maximumTourismSet = set()


def maximumTourism():
    import collections
    d = collections.defaultdict(set)
    for _ in range(int(input().split()[1])):
        a, b = map(int, input().split())
        d[a].add(b)
        d[b].add(a)
        # [d[a].add(i) for i in d[b]]
        # [d[b].add(i) for i in d[a]]
    maxval = 0
    for k in d.keys():
        if k not in maximumTourismSet:
            maxval = max(maxval, bfsMap(k, d))
    print(maxval)


def bfsMap(k, d):
    count = 0
    q = [k]
    global maximumTourismSet
    maximumTourismSet.add(k)
    while q:
        for nextNode in d[q.pop()]:
            if nextNode not in maximumTourismSet:
                q.append(nextNode)
            maximumTourismSet.add(nextNode)
        count += 1

    return count


def maxScore():
    import itertools
    _ = input()
    nums = set(map(int, input().split()))
    print([i % j for i in nums for j in nums])
    sumVal = sum(nums)
    maxSc = 0
    while sumVal > 0:
        k = -1
        delv = 0
        for i in nums:
            if k < (sumVal - i) % i:
                k = (sumVal - i) % i
                delv = i
        nums.remove(delv)
        maxSc += k
        sumVal -= delv
    print(maxSc)


def cultureConference():
    d = collections.defaultdict(set)
    count = 1
    burnedOut = set()
    for _ in range(int(input())):
        pred, burn = map(int, input().split())
        d[count].add(pred)
        d[pred].add[count]
        if burn > 0 :
            burnedOut.add(count)

def countRemove(k, d, b):
    visited = set()
    visited.add(k)
    while b:



import collections
maxScore()
