"""
题目描述：
    给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
    你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
    返回获得利润的最大值。
    注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
示例：
    输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
    输出: 8
    解释: 能够达到的最大利润:  
    在此处买入 prices[0] = 1
    在此处卖出 prices[3] = 8
    在此处买入 prices[4] = 4
    在此处卖出 prices[5] = 9
    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
提示：
    0 < prices.length <= 50000.
    0 < prices[i] < 50000.
    0 <= fee < 50000.
题解：
    1、动态规划
    主要重点在于每一天的状态可以分为持有股票和没持有两种
    因此用dp[i][0]和dp[i][1]分别代表第i天没持有和持有股票的最佳收益
    而后分析它们和前一天的最佳收益的关系即可（诶，感觉自己就是脑子不灵光）
    2、贪心算法
    ...
"""

def maxProfit(prices, fee):
    if len(prices) < 2:
        return 0
    m = len(prices)
    dp = [[0 for i in range(2)] for i in range(m)]
    dp[0][1] = -prices[0]
    for i in range(1, m):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    return dp[m-1][0]

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(maxProfit(prices, fee))
