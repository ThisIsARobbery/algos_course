
def min_coins(n, coins):
    coins = coins.copy()
    coins.sort(reverse=True)
    results = []
    k = 0
    for i in range(len(coins)):
        if coins[i] <= n:
            k += n // coins[i]
            for _ in range(n // coins[i]):
                results.append(coins[i])
            n = n % coins[i]

    print("%d coins" % k)
    for elem in results:
        print(elem, end=' ')

N = int(input())
print(N)
min_coins(N, [1, 5, 10, 25])