"""
题目描述：
    在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
    例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
    分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。
    上例中的 "xxxx" 分组用区间表示为 [3,6] 。
    我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
    找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
示例：
    输入：s = "abbxxxxzzy"
    输出：[[3,6]]
    解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
提示：
    1 <= s.length <= 1000
    s 仅含小写英文字母
"""

def largeGroupPositions(s):
    m, res = len(s), []
    if m < 3:
        return res
    else:
        sim, index, i = s[0], 0, 1
        while i < m:
            while i < m and s[i] == sim:
                i += 1
            if i - index >= 3:
                res.append([index, i-1])
            if i < m and s[i] != sim:
                sim, index = s[i], i
        return res

s = "abbxxxxzzy"
print(largeGroupPositions(s))