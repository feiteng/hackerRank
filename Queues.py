def Queue_using_Two_Stacks():
    s1 = []
    s2 = []
    for _ in range(int(input())):
        ops = list(map(int, input().split()))
        if ops[0] == 1:
                s1.append(ops[1])
        elif ops[0] == 2:
            if not s2:
                while s1:
                    s2.append(s1.pop())
            s2.pop()
        elif ops[0] == 3:
            if not s2:
                while s1:
                    s2.append(s1.pop())
            print(s2[-1])
Queue_using_Two_Stacks()
