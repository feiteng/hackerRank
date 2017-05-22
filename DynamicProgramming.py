def The_Coin_Change_Problem():
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], n + 1):
            ways[j] += ways[j - coins[i]]
    print(ways[n])


def The_Longest_Common_Subsequence():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


def Equal():
    for _ in range(int(input())):
        q = input()
        n = list(map(int, input().split()))
        minval = min(n)
        minvals = [i - minval for i in n]
        count = sum(op(m) for m in minvals)
        # print(count)
        for i in [1, 1, 3]:
            minvals = [m + i for m in minvals]
            nextcount = sum(op(m) for m in minvals)
            count = min(count, nextcount)
        print(count)


def op(n):
    coins = [1, 2, 5]
    count = 0
    count += n // 5
    n %= 5
    count += n // 2
    n %= 2
    count += n
    return count


def Fibonacci_Modified():
    a0, a1, n = map(int, input().split())
    for i in range(n - 2):
        a2 = a0 + a1 ** 2
        a0 = a1
        a1 = a2
    print(a2)


def Sherlock_and_Cost():
    for _ in range(int(input())):
        n = int(input())
        b = list(map(int, input().split()))
        if (n < 2):
            print(0)
            continue
        p = [0]
        np = [0]
        for i in range(1, n):
            p.append(max(b[i] - 1 + np[i - 1], p[i - 1]))
            np.append(max(p[i - 1] + b[i - 1] - 1, np[i - 1]))
        print(max(p[-1], np[-1]))


def Vertical_Sticks():
    for _ in range(int(input())):
        n = int(input())
        c = list(map(int, input().split()))
        v = []
        for i in c:
            v.append(sum([1 if i <= j else 0 for j in c]))
        count = 0
        for i in v:
            count += (n + 1) / (i + 1)
        print('{0:.2f}'.format(count))


def Candies():
    candyCount = []
    for _ in range(int(input())):
        candyCount.append((int(input())))
    ratings = [1 for _ in range(len(candyCount))]
    print(candy(candyCount))


def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    candies = [1 for _ in range(len(ratings))]
    for i in range(len(candies) - 1):
        if ratings[i] < ratings[i + 1]:
            candies[i + 1] = candies[i] + 1
    for i in range(len(candies) - 1, 0, -1):
        if ratings[i] < ratings[i - 1]:
            candies[i - 1] = max(candies[i - 1], candies[i] + 1)
    # print(candies)
    return sum(candies)


def Sam_and_substrings():
    s = input()
    count = 0
    factor = 1
    k = 1
    for i in range(len(s)-1,-1,-1):
        n = int(s[i])
        count += n * (i+1) * factor % 1000000007
        factor = (factor*10+1) % 1000000007
    print(count % 1000000007)


import time
t = time.time()

Sam_and_substrings()

print(time.time()-t)
