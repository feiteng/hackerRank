import itertools
import numpy as np
import matplotlib.pyplot as plt
import math


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Solution:
    def print_rangoli(size):
        if size == 1:
            print('a')
            return
        row = size * 2 - 1
        col = row * 2 - 1
        lastChar = chr(ord('a') + size - 1)
        for i in range(1, row + 1, 2):
            space = i * 2 - 1
            s = '-' * ((col - space) // 2)
            for j in range(0, (i + 1) // 2):
                s += chr(ord(lastChar) - j) + '-'
            s += s[:len(s) - 3][::-1]
            print(s)
        for i in range(row - 2, 0, -2):
            space = i * 2 - 1
            s = '-' * ((col - space) // 2)
            for j in range(0, (i + 1) // 2):
                s += chr(ord(lastChar) - j) + '-'
            s += s[:len(s) - 3][::-1]
            print(s)


    def capitalize(string):
        s = string.split(' ')
        for i in range(0, len(s)):
            if s[i].isalpha():
                s[i] = s[i].title()
        return ' '.join(s)


    def minion_game(string):
        # indices of constants and vowels
        stringVowels = []
        stringConstants = []
        vowels = 'AEIOU'
        for i in range(0, 26):
            c = chr(ord('A') + i)
            index = 0
            if c in vowels: continue
            while index < len(string):
                index = string.find(c, index)
                if index == -1:
                    break
                stringConstants.append(index)
                index += 1

        for v in vowels:
            index = 0
            while index < len(string):
                index = string.find(v, index)
                if index == -1:
                    break
                stringVowels.append(index)
                index += 1
        subStringV = set([string[i:k] for i in stringVowels for k in range(i + 1, len(string) + 1)])
        subStringC = set([string[i:k] for i in stringConstants for k in range(i + 1, len(string) + 1)])
        countv = 0
        countc = 0
        import re
        for subv in subStringV:
            countv += len(re.findall('(?=' + subv + ')', string))
        for subc in subStringC:
            countc += len(re.findall('(?=' + subc + ')', string))
        if countv > countc:
            print("Kevin " + str(countv))
        if countc > countv:
            print("Stuart " + str(countc))
        if countc == countv:
            print("Draw")


    def merge_the_tools(string, k):
        n = len(string)
        step = n // k
        s = list(string)
        for i in range(0, n, k):
            l = []
            print(s[i:i + k])
            for i in s[i:i + k]:
                if i in l:
                    continue
                else:
                    l.append(i)
            print(''.join(l))


    def average(array):
        # your code goes here
        uniqueArray = set(array)
        avg = sum(uniqueArray) / len(uniqueArray)
        print(avg)


    def groupby():
        import itertools
        s = input()
        for k, g in itertools.groupby(s):
            print(k)
            print(list(g))


    def f(x, m):
        k, m = map(int, input().split())
        lists = []
        lists.extend(list(map(int, input().split()[1:])) for _ in range(k))
        # for x in lists:
        #     print(list(x))
        print(max(map(lambda x: sum(a ** 2 for a in x) % m, list(itertools.product(*lists)))))


    import collections


    def counter():
        _ = input()
        shoes = collections.Counter(list(map(int, input().split())))
        n = int(input())
        shoePrice = [list(map(int, input().split())) for _ in range(n)]
        count = sum([shoe[1] if shoes[shoe[0]] > 0 else 0 for shoe in shoePrice])
        print(count)


    def defDict():
        import collections
        n, m = map(int, input().split())
        d = collections.defaultdict(list)
        for i in range(1, n + 1): d[input()].append(i)
        print(d[input()] for _ in range(m))


    def namedTup():
        import collections
        n = int(input())
        pos = list(input().split()).index('MARKS')
        marks = [int(input().split()[pos]) for _ in range(n)]
        print(sum(marks) / n)


    def orderedDict():
        import collections
        d = collections.OrderedDict()
        n = int(input())
        for _ in range(n):
            inp = input().split()
            key = ' '.join(inp[0:len(inp) - 1])
            if key in d:
                d[key] += int(inp[-1])
            else:
                d[key] = int(inp[-1])
        for k in d:
            print(k, d[k])


    def wordOrder():
        import collections
        d = collections.OrderedDict()
        n = int(input())
        for _ in range(n):
            key = input()
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
        print(len(d.keys()))
        for k in d:
            print(d[k], end=' ')


    def mostCommon():
        import collections
        d = collections.Counter(input())
        sorted_d = sorted(d.items(), key=lambda t: (-t[1], t[0]))
        for i in range(0, 3, 1):
            print(' '.join(map(str, sorted_d[i])))


    def calendarModule():
        import calendar
        m, d, y = map(int, input().split())
        print(calendar.day_name[calendar.weekday(y, m, d)].upper())


    def timeDelta():
        from datetime import datetime
        n = int(input())
        parseFormat = '%a %d %b %Y %H:%M:%S %z'
        for _ in range(n):
            # Day dd Mon yyyy hh:mm:ss +xxxx
            t1 = datetime.strptime(input(), parseFormat)
            t2 = datetime.strptime(input(), parseFormat)
            print(int(math.fabs((t1 - t2).total_seconds())))


    def exception():
        for _ in range(int(input())):
            try:
                a, b = map(int, input().split())
                print(a // b)
            except ZeroDivisionError as e:
                print("Error Code:", e)
            except ValueError as e:
                print("Error Code:", e)


    def regex():
        import re
        for _ in range(int(input())):
            try:
                re.compile(input())
                print('True')
            except re.error:
                print('False')


    def zipped():
        n, x = map(int, input().split())
        score = [list(map(float, input().split())) for _ in range(x)]
        print(' '.join([sum(s) / x]) for s in list(zip(*score)))


    def fun(s):
        import re
        if re.match('[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s): return True
        return False

        # return True if s is a valid email, else return False


    def filter_mail(emails):
        return list(filter(fun, emails))


    def checkEmail():
        n = int(input())
        emails = []
        for _ in range(n):
            emails.append(input())
        filtered_emails = filter_mail(emails)
        filtered_emails.sort()
        print(filtered_emails)


    def re():
        import re
        for _ in range(int(input())):
            num = input()
            if re.match('\+?[0-9]?\[.0-9]+', num):
                print("True")
            else:
                print("False")


    def numpyArray():
        import numpy
        print(numpy.array(list(input().split())[::-1], float))


    def onesZeros():
        import numpy

        size = list(map(int, input().split()))
        z = numpy.zeros(size, dtype=numpy.int)
        o = numpy.ones(size, dtype=numpy.int)

        print(z)

        print(o)


    def algoCrush():
        import operator
        m, n = map(int, input().split())
        r = [0] * (m + 1)
        for _ in range(n):
            a, b, v = map(int, input().split())
            r[a] += v
            if b + 1 < m + 1: r[b + 1] += -v
        count = 0
        sum = 0
        for i in range(1, m + 1):
            sum += r[i]
            count = max(count, sum)
        print(count)


    def calcI(I, pi, pj):
        count = 0
        for i in range(0, 3):
            count += I[pi][pj + i]
        count += I[pi + 1][pj + 1]
        for i in range(0, 3):
            count += I[pi + 2][pj + i]
        return count


    def SortedInsert(head, data):
        if head == None: return Node(data)
        tmp = head
        while tmp.next != None and tmp.data < data:
            tmp = tmp.next
        newNode = Node(data, tmp, tmp.next)
        tmp.next = newNode
        tmp.next.prev = newNode
        return head


    def circularArray():
        # !/bin/python3

        import sys

        n, k, q = input().strip().split(' ')
        n, k, q = [int(n), int(k), int(q)]
        a = [int(a_temp) for a_temp in input().strip().split(' ')]
        a = a[-(k % n):] + a
        for a0 in range(q):
            m = int(input().strip())
            print(a[m])


    def compareTrip():
        # !/bin/python3

        import sys

        a0, a1, a2 = input().strip().split(' ')
        a0, a1, a2 = [int(a0), int(a1), int(a2)]
        b0, b1, b2 = input().strip().split(' ')
        b0, b1, b2 = [int(b0), int(b1), int(b2)]

        alice = 0
        bob = 0
        if a0 > b0:
            alice += 1
        if a1 > b1:
            alice += 1
        if a2 > b2:
            alice += 1
        if a0 < b0:
            bob += 1
        if a1 < b1:
            bob += 1
        if a2 < b2:
            bob += 1
        print(str(alice) + ' ' + str(bob))


    def minmaxCalc():
        l = list(map(int, input().split()))
        l.sort()
        print('{} {}'.format(sum(l[:len(l) - 1]), sum(l[1:])))


    def pdfViewer():
        h = list(map(int, input().strip().split(' ')))
        word = input().strip()
        print(max(h[ord(w) - ord('a')] for w in word) * len(word))


    def appleOrange():
        s, t = input().strip().split(' ')
        s, t = [int(s), int(t)]
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        m, n = input().strip().split(' ')
        m, n = [int(m), int(n)]
        apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
        orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

        print(sum([a + ap >= s and a + ap <= t for ap in apple]))
        print(sum([b + ora >= s and b + ora <= t for ora in orange]))


    def kangaroo():
        x1, v1, x2, v2 = input().strip().split(' ')
        x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
        if v1 == v2 and x1 != x2:
            print('NO')
            return
        t = (x2 - x1) // (v1 - v2)
        if t >= 0 and t * (v1 - v2) == x2 - x1:
            print('YES')
        else:
            print('NO')


    def twoSets():
        import operator, functools
        n, m = map(int, input().strip().split(' '))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        l = []
        for i in range(a[-1], b[0] + 1):
            if all([True if i % anum == 0 and bnum % i == 0 else False for anum in a for bnum in b]):
                l.append(i)
        print(len(l))


    def divisibleSum():
        import itertools
        n, k = map(int, input().split(' '))
        a = list(map(int, input().split()))
        print(sum([(a[i] + a[j]) % k == 0 for (i, j) in itertools.combinations(range(n), 2)]))


    def bonAppetite():
        n, k = map(int, input().split())
        price = list(map(int, input().split()))
        charge = int(input())
        fairPrice = (sum(price) - price[k]) // 2
        print('Bon Appetit' if fairPrice == charge else charge - fairPrice)


    def sellSocks():
        import collections
        _ = input()
        c = collections.Counter(list(map(int, input().split())))
        print(sum(k // 2 for k in c.values() if k // 2 > 0))


    def beautifulDays():
        i, j, k = map(int, input().split())
        print(len([d for d in range(i, j + 1) if abs(d - reversed(d)) % k == 0]))


    def viralAd():
        n = int(input())
        l = [5]
        [l.append(l[-1] // 2 * 3) for _ in range(n - 1)]
        print(sum(map(lambda x: x // 2, l)))


    def savePrisoner():
        for _ in range(int(input())):
            n, m, s = map(int, input().split())
            num = (s + m % n - 1) % n
            if num == 0:
                print(n)
            else:
                print(num)


    class Solution(object):
        def grayCode(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            if n == 0: return [0]
            l = [0, 1]
            if n == 1: return l
            [l.extend(map(lambda x: x ^ 2 ** i, l[::-1])) for i in range(1, n)]
            return l


    def jumpOnClouds():
        n, k = map(int, input().split())
        cloud = list(map(int, input().split()))
        start = 0
        e = 100
        nextStep = k % n
        while nextStep != start:
            e -= 1
            e -= 2 if cloud[nextStep] > 0 else 0
            nextStep = (nextStep + k) % n
        e -= 1
        e -= 2 if cloud[nextStep] > 0 else 0
        print(e)


    def appendDelete():
        s = input()
        t = input()
        k = int(input())
        c = min(len(s), len(t))
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                c = i
                break
        minMove = len(s) + len(t) - 2 * c
        if minMove > k:
            print('No')
            return
        if (k - minMove) % 2 == 0:
            print('Yes')
            return
        if len(s) + len(t) <= k:
            print('Yes')
            return
        print('No')


    def nonDivisibleSubset():
        import itertools, collections
        n, k = map(int, input().split())
        count = collections.Counter([*map(lambda x: x % k, map(int, input().split()))])
        total = 0
        print(count)
        for i in range(1, k // 2 + 1):
            if i == k - i:
                continue
            total += max(count[i], count[k - i])
        if count[0] != 0: total += 1
        if k % 2 == 0 and count[k // 2] != 0: total += 1
        print(total)


    def repeatingString():
        import itertools, collections
        s = input()
        n = int(input())
        k = s.count('a')
        print(n // len(s) * k + s[:n - n // len(s) * len(s) + 1].count('a'))


    def jumpingClounds():
        n = int(input())
        clouds = list(map(int, input().split()))
        initialPos = n - 1
        count = 0
        while initialPos >= 1:
            if clouds[initialPos - 2] != 1:
                initialPos -= 2
            else:
                initialPos -= 1
            count += 1
        print(count + 1)


    def equalizeArray():
        import collections
        _ = input()
        s = list(map(int, input().split()))
        counter = collections.Counter(s)
        print(len(s) - max(counter.values()))


    def taumAndBday():
        t = int(input())
        for _ in range(t):
            b, w = map(int, input().split())
            x, y, z = map(int, input().split())
            print(b * min(x, y + z) + w * min(y, x + z))


    def beautifulTrip():
        n, k = map(int, input().split())
        vals = list(map(int, input().split()))
        d = {i: 1 for i in vals}
        l = [i for i in d.keys() if i - k in d and i + k in d]
        print(len(l))


    def biggerIsGreater():
        for _ in range(int(input())):
            s = input()
            sList = list(s)
            sNew = nextPerm(sList)
            print('no answer' if sNew <= s else sNew)


    def nextPerm(list):
        try:
            pos = len(list) - 2 - [x >= y for (x, y) in zip(list[:-1], list[1:])][::-1].index(False)
        except ValueError:
            return ''.join(list)
        nextPos = pos + 1
        for i in range(len(list) - 1, pos, -1):
            if list[i] > list[pos]:
                nextPos = i
                break
        tmp = list[pos]
        list[pos] = list[nextPos]
        list[nextPos] = tmp
        list = list[:pos + 1] + list[-1:pos:-1]
        return ''.join(list)


    def minDistance():
        import collections
        size = int(input())
        arr = [*map(int, input().split())]
        d = collections.defaultdict(list)
        dmin = size
        [d[a].append(pos) for pos, a in enumerate(arr)]
        if all(len(k) < 2 for k in d.values()):
            print(-1)
            return
        for k in d.values():
            if len(k) < 2: continue
            # print([a - b for (a, b) in zip(k[1:], k[:-1])])
            dmin = min(dmin, min([a - b for (a, b) in zip(k[1:], k[:-1])]))
        print(dmin)


    def cavityMap():
        size = int(input())
        l = [[*map(int, list(input()))] for _ in range(size)]
        lNew = []
        for i in range(size):
            lNew.append([l[i][j] if i == 0 or i == size - 1 or j == 0 or j == size - 1
                         else 'x' if l[i][j] > l[i][j - 1] and l[i][j] > l[i][j + 1] and
                                     l[i][j] > l[i + 1][j] and l[i][j] > l[i - 1][j]
            else l[i][j] for j in range(size)])
        for litem in lNew:        print(''.join([*map(str, litem)]))


    def chocolateFeast():
        for _ in range(int(input())):
            count = 0
            n, c, m = map(int, input().split())
            numWrappers=  n // c
            count = numWrappers
            while numWrappers >= m:
                wrappersLeft = numWrappers % m
                numWrappers = numWrappers // m
                count += numWrappers
                numWrappers += wrappersLeft
            print(count)


    def serviceLane():
        n, t = map(int, input().split())
        width = list(map(int, input().split()))
        for _ in range(t):
            start, end = map(int, input().split())
            print(min(width[start - 1:end + 1]))


    def theGridSearch():
        import re
        for _ in range(int(input())):
            a = [input() for _ in range(int(input().split()[0]))]
            b = [input() for _ in range(int(input().split()[0]))]

            for aElem in a:
                print([m.start() for m in re.finditer(b[0], aElem)])
            # posList = [(pos,found) for pos, found in enumerate(re.finditer(b[0],aElem) for aElem in a) if pos <= len(a)-len(b)]
            # posList = [(pos, found) for pos, found in enumerate(aElem.find(b[0]) for aElem in a) if found > 0 and pos <= len(a) - len(b)]
            # print(pos, found[0] for pos, found in posList)
            # flag = True
            # for (i, pos) in posList:
            #     matches = [a[i + k].find(b[k]) == pos for k in range(len(b))]
            #     if all(matches):
            #         print('YES')
            #         flag= False
            #         break
            # if flag: print('NO')


    def maximumSubarraySum():
        for _ in range(int(input())):
            a, k = map(int, input().split())
            n = list(map(int, input().split()))
            s = 0
            si = k
            sj = 0
            for ni in n:
                s += ni
                si = min(si, s % k)
                newRemain = s % k - si
                if newRemain < 0 :
                    newRemain += k
                sj = max(sj, newRemain)
            print(sj)

    def minimumTotal(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            if len(triangle) < 2: return min(triangle[0])
            for i in range(len(triangle)-1):
                l1 = triangle[i]
                l2 = triangle[i + 1]
                l2[0] += l1[0]
                l2[-1] += l1[-1]
                for j in range(1, len(l2) - 1):
                    l2[j] = min(l1[j - 1], l1[j]) + l2[j]
                print(l2)
            return min(triangle[-1])

l = [[-1], [2, 3], [1, -1, -3]]
s = Solution()

print(s.minimumTotal(l))

