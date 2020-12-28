def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    def calDp(n):
        if n == 0:  return 0
        if n < 0:  return -1
        if dp[n] != float('inf'):  return dp[n]
        res = float('inf')
        for coin in coins:
            subproblem = calDp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)
        dp[n] = res if res != float('inf') else -1
        return dp[n]
    return calDp(amount)

coins = [1, 2, 5, 7]
amount = 11
print(coinChange(coins, amount))