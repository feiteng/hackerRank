class Solution:
    def q1(self):
        a, s, f = map(int, input().split())
        count = 0
        a = min(a, 10)
        s = min(s, 10)
        f = min(f, 10)
        count = (a + s + f) * 10
        print(count)

    def q2(self):
        _ = input()
        vals = list(map(int, input().split()))
        count = [0] * len(vals)
        i = 0
        j = 0
        while j < len(vals) - 1:
            i = j
            while i < len(vals) - 1 and vals[i] < vals[i + 1]:
                i += 1
            count[j] += max(i - j - 1, 0)
            j = i + 1
        i = 0
        j = 0
        print(count)
        while j < len(vals) - 1:
            i = j
            while i < len(vals) - 1 and vals[i] > vals[i + 1]:
                i += 1
            count[j] += max(i - j - 1, 0)
            j = i + 1
        # print(count)
        print(sum(count))

    def q3(self):
        n, k = map(int, input().split())
        l = [int(input()) for _ in range(n)]
        import itertools, functools, collections
        d = collections.defaultdict(dict)
        res = []
        for comb in itertools.combinations(l, k):
            m = 0xffffffff
            for i in list(comb):
                if not d[m] or i not in d[m] :
                    d[m][i] = m & i
                m = d[m][i]
            res.append(m)
        resCount = collections.Counter(res)
        print("{}\n{}".format(max(res), resCount[max(res)]%(10**9+7)))


s = Solution()
s.q3()
