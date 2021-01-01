"""
题目描述：
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1。你可以认为每种硬币的数量是无限的。
示例：
    输入：coins = [1, 2, 5], amount = 11
    输出：3 
    解释：11 = 5 + 5 + 1
"""

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