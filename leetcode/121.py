"""
题目描述：
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
示例：
    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
题解：
    1、自己想的（其实就是动态规划好像）
    一个变量记录当前的最低价格，其构成为先前的最小值和当前股票价格前一天价格
    另一个变量记录最大获利，其构成为先前最大获利和当前价格减去最小价格
    因为最低价格的股票天数永远小于计算获利卖出时股票价格的天数，所以计算的获利正确
"""

def maxProfit(prices):
    min_price, profit = float('inf'), 0
    for i in range(1, len(prices)):
        min_price = min(prices[i-1], min_price)
        profit = max(profit, prices[i] - min_price)
    return profit

prices = [2, 5, 1, 3]
print(maxProfit(prices))