"""
题目描述：
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
    计算其二进制数中的 1 的数目并将它们作为数组返回。
示例：
    输入: 5
    输出: [0,1,1,2,1,2]
题解：
    1、动态规划 + 进制转换算法
    分析求解比特位的方法，就是不断除2取余，因此dp[i] = dp[i // 2] + i % 2
    时间复杂度O(n)
"""

def countBits(num):
    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        dp[i] += dp[i // 2] + i % 2
    return dp

if __name__ == '__main__':
    print(countBits(5))