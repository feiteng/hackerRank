def Qheap1():
    h = []  # min heap
    for _ in range(int(input())):
        ops = list(map(int, input().split()))
        if ops[0] == 1:
            h.append(ops[1])
            heapifyUp(h, len(h) - 1)
        elif ops[0] == 2:
            pos = h.index(ops[1])
            h[pos] = h[len(h) - 1]
            h.pop()
            heapifyDown(h, pos)
            heapifyUp(h, pos)
        elif ops[0] == 3:
            print(h[0])


def heapifyUp(h, pos):
    if not h or pos == 0 or pos == len(h): return
    while pos > 0 and h[pos] < h[(pos - 1) // 2]:  # and pos < len(h)
        t = h[(pos - 1) // 2]
        h[(pos - 1) // 2] = h[pos]
        h[pos] = t
        pos = (pos - 1) // 2


def heapifyDown(h, pos):
    if not h or pos == len(h): return
    left = pos * 2 + 1
    right = left + 1
    while left < len(h) and right < len(h):
        if h[left] < h[pos] or h[right] < h[pos]:
            if h[left] < h[right]:
                minPos = left
            else:
                minPos = right
            t = h[pos]
            h[pos] = h[minPos]
            h[minPos] = t
            pos = minPos
        else:
            return
        left = pos * 2 + 1
        right = left + 1
    if left < len(h) and h[left] < h[pos]:
        t = h[pos]
        h[pos] = h[left]
        h[left] = t


def Jesse_and_Cookies():
    import heapq
    n, k = map(int, input().split())
    sweetness = sorted(list(map(int, input().split())))
    count = 0
    while sweetness[0] < k:
        # print(sweetness)
        if not sweetness: break
        a = heapq.heappop(sweetness)
        if not sweetness: break
        b = heapq.heappop(sweetness)
        heapq.heappush(sweetness, a + 2 * b)
        count += 1
    if sweetness:
        print(count)
    else:
        print(-1)


def Find_the_Running_Median():
    import heapq
    small = []
    big = []
    for _ in range(int(input())):
        heapq.heappush(big, int(input()))
        if len(big) > 1 + len(small):
            heapq.heappush(small, -heapq.heappop(big))
        elif small and big[0] < -small[0]:
            heapq.heappush(small, -heapq.heappop(big))
            heapq.heappush(big, -heapq.heappop(small))
        if len(big) != len(small):
            print('{:.1f}'.format(big[0]))
        else:
            print('{:.1f}'.format((-small[0] + big[0]) / 2))


def Minimum_Average_Waiting_Time():
    swtimes = [list(map(int, input().split()))for _ in range(int(input()))]
    swtimes2 = sorted(swtimes, key = lambda x : x[0])
    print(swtimes)
    print(swtimes2)

Minimum_Average_Waiting_Time()
