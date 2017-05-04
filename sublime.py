def serviceLane():
    n, t = map(int,input().split())
    width = list(map(int,input().split()))
    for _ in range(t):
        start, end = map(int,input().split())
        print(min(width[start-1:end+1]))


def theGridSearch():
    for _ in range(int(input())):
        a = [[input()] for _ in range(int(input().split()[0]))]
        b = [[input()] for _ in range(int(input().split()[0]))]
        print(a)
        print(b)

theGridSearch()