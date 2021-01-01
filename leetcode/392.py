"""
题目描述：
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    字符串的一个子序列是原始字符串删除一些（也可以不删除）
    字符而不改变剩余字符相对位置形成的新字符串。
    （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
    如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，
    你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
示例：
    输入：s = "axc", t = "ahbgdc"
    输出：false
题解：
    1、双指针法
    时间复杂度O(len(s) + len(t))
    空间复杂度O(1)
    2、动态规划法
    在双指针法中，大量时间被耗费在搜寻下一个匹配字符上，如果我们能建立一张
    映射表记录t中每个字符的位置，那么对于处理大量相同问题就可以减少许多时间。
    因此可以利用动态规划，设函数f[i][j]表示字符串中从位置 i 开始往后字符 j 第一次出现的位置。
    在状态转移中，如果t中位置 i 的字符就是 j，那么f[i][j] = i，否则 j 出现在位置 i + 1开始往后，即
    f[i][j] = f[i+1][j]，因此我们要倒过来进行动态规划（正向解不了啊诶），从后往前枚举 i。下面是状态转移方程：
        f[i][j] = i if t[i] == j else f[i+1][j]
    假设下标从0开始，那么f[i][j]中有 0 <= i <= m - 1，为了处理边界f[m-1][...]，我们可以置f[m][...]为m，这样即可以
    让f[m-1][...]正常进行转移。而后判断时即可以判断f[i][j] 是否等于 m 来判断从位置 i 后是否存在字符 j 。
    这样，我们就可以利用f数组，每次O(1)地跳转到下一个位置，直至位置变为 m 或 s 中每个字符都匹配成功。
        时间复杂度O(len(t) * |letters| + k * len(s)) // 对于 k 个子字符串 s 输入，letters为字符集，本题中为小写字母，为26
        空间复杂度O(len(t) * |letters|)
"""

def isSubsequence(s, t):
    # 双指针法
    # if s is '':
    #     return True
    # slen, tlen = len(s), len(t)
    # if slen > tlen:
    #     return False
    # si, ti = 0, 0
    # while si < slen and ti < tlen:
    #     if s[si] == t[ti]:
    #         si += 1
    #         ti += 1
    #     else:
    #         ti += 1
    # return si == slen

    # 动态规划法
    slen, tlen = len(s), len(t)
    f = [[0] * 26 for _ in range(tlen)]
    f.append([tlen] * 26)

    for i in range(tlen-1, -1, -1):
        for j in range(26):
            f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]
    
    add = 0
    for i in range(slen):
        if f[add][ord(s[i]) - ord('a')] == tlen:
            return False
        else:
            add = f[add][ord(s[i]) - ord('a')] + 1
    
    return True

s = 'axc'
t = 'ahbgdc'
print("s = %s, t = %s, result = %s" %(s, t, isSubsequence(s, t)))
