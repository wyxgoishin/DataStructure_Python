"""
题目描述：
    给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
    字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。
示例：
    输入：n = 2
    输出：15
    解释：仅由元音组成的 15 个字典序字符串为
    ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
    注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
"""

def countVowelStrings(n):
    # # 空间未优化的二维dp
    # # i 代表后续可选有序元音数-1
    # # j 代表可组成成多少长度的字符
    # f = [[0 for x in range(n+1)] for x in range(5)]
    # for i in range(5):
    #     f[i][0] = 0
    #     f[i][1] = i + 1
    
    # for i in range(5):
    #     for j in range(2, n+1):
    #         if i == 0:
    #             f[i][j] = 1
    #         else:
    #             f[i][j] = sum(f[i-x][j-1] for x in range(i+1))    
    # return f[4][n]

    # 空间优化后的二维dp，参考27行的状态转移方程，f[i][j] 只和 f[i-x][j-1]有关，因此只要记录5个变量即可
    # 相比上面空间复杂度大大减少
    f1, f2, f3, f4, f5 = 1, 2, 3, 4, 5
    for i in range(2, n+1):
        f1, f2, f3, f4, f5 = f1, f1 + f2, f3 + f2 + f1, f4 + f3 + f2 + f1,  f5 + f4 + f3 + f2 + f1
    return f5

    # 上面一串代码的等价写法
    # dp = [1] * 5
    # res = 0
    # for i in range(1, n):
    #     for j in range(1, 5):
    #         dp[j] += dp[j-1]
    
    # for i in range(len(dp)):
    #     res += dp[i]

    # return res

n = 5
print(countVowelStrings(n))