"""
题目描述：
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
    对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，
    都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会
    得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
提示：
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1
"""

def findContentChildren(g, s):
    # 暴力穷举法
    g.sort()
    s.sort()
    pre_child, num = 0, 0
    for i in range(len(s)):
        if pre_child >= len(g):
            break
        for j in range(pre_child, len(g)):
            if g[j] <= s[i]:
                num += 1
                pre_child = j + 1
                break
    return num

g = [1, 2, 3]
s = [1, 4]
print(findContentChildren(g, s))