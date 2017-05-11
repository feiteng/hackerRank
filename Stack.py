def gameOfTwoStacks():
    for _ in range(int(input())):
        n, m, x = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        sa = [0]
        sb = [0]
        [sa.append(sa[-1] + i) for i in a]
        [sb.append(sb[-1] + i) for i in b]
        while sa[-1] > x:
            sa.pop()
        k = len(sa) - 1
        i = 0
        while sa:
            while i < len(sb) and sa[-1] + sb[i] <= x:
                i += 1
            k = max(k, len(sa) - 1 + i - 1)
            sa.pop()
        print(k)


def Largest_Rectangle():
    _ = input()
    h = list(map(int, input().split()))
    stack = []
    size = 0
    i = 0
    while i < len(h):
        if not stack or h[i] > h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = h[stack.pop()]
            length = i if not stack else i - 1 - stack[-1]
            size = max(size, top * length)
    while stack:
        top = h[stack.pop()]
        length = i if not stack else i - 1 - stack[-1]
        size = max(size, top * length)
    print(size)


gameOfTwoStacks()
