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


def Simple_Text_Editor():
    s = ['']
    for _ in range(int(input())):
        inp = input().split()
        if inp[0] == '1':
            s.append(s[-1] + inp[1])
        if inp[0] == '2':
            s.append(s[-1][:-int(inp[1])])
        if inp[0] == '3':
            print(s[-1][int(inp[1]) - 1])
        if inp[0] == '4':
            s.pop()


def Waiter():
    n, q = map(int, input().split())
    primes = waiterSievePrime_1200()
    p = list(map(int, input().split()))
    a = [[] for _ in range(q + 1)]
    a[0] = p
    b = [[] for _ in range(q + 1)]
    for i in range(q):
        prime = primes[i]
        for k in a[i][::-1]:
            if k % prime == 0:
                b[i + 1].append(k)
            else:
                a[i + 1].append(k)
    for b0 in b[1:]:
        if b0:
            print('\n'.join(map(str, b0[::-1])))
    print('\n'.join(map(str, a[q][::-1])))


def waiterSievePrime_1200():
    primes = list(range(10000))
    check = [True] * len(primes)
    check[0] = check[1] = False
    for i in range(len(primes)):
        if check[i]:
            k = 2
            while primes[i] * k < 10000:
                check[primes[i] * k] = False
                k += 1
    leftPrime = [i for (i, j) in zip(primes, check) if j]
    # print(leftPrime)
    # print(len(leftPrime))
    return leftPrime[:1200]


def Poisonous_Plants():
    _ = input()
    plants = list(map(int, input().split()))
    stack = [[plants[0]]]
    k = 1
    while k < len(plants):
        while k < len(plants) and stack[-1][-1] >= plants[k]:
            stack[-1].append(plants[k])
            k += 1
        if k < len(plants):
            stack.append([plants[k]])
            k += 1
    c = 0
    countDel = 1
    while countDel > 0:
        countDel = 0
        for i in range(len(stack) - 1, 0, -1):
            if stack[i - 1][-1] < stack[i][0]:
                stack[i].pop(0)
                countDel += 1
            if not stack[i]:
                stack.pop(i)
        c += 1 if countDel > 0 else 0
    print(c)


def AND_xor_OR():
    _ = input()
    n = list(map(int, input().split()))



def andXorOrCalc(m, n):
    return (((m&n)^(m|n))&(m^n)) # = m ^ n


Poisonous_Plants()
