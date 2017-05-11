def The_Coin_Change_Problem():
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], n + 1):
            ways[j] += ways[j - coins[i]]
    print(ways[n])


The_Coin_Change_Problem()
