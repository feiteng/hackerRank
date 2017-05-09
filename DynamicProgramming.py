def The_Coin_Change_Problem():
    n, m = map(int,input().split())
    coins = sorted(list(map(int, input().split())))
    values = [0]*(n+1)
    for coin in coins:
        values[coin] = 1
    values[0] = 1
    for i in range(len(values)):
        for j in range(len(coins)):
            if i // 2 >= coins[j]:
                values[i] += values[i-coins[j]] * values[coins[j]]
            else:
                break
    print(values[n])

The_Coin_Change_Problem()