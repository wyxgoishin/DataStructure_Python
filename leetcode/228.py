"""
题目描述：
    给定一个无重复元素的有序整数数组 nums 。返回恰好覆盖数组中所有数字的最小有序区间范围列表。
    也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
    列表中的每个区间范围 [a,b] 应该按如下格式输出：
        "a->b" ，如果 a != b
        "a" ，如果 a == b
示例：
    输入：nums = [0,1,2,4,5,7]
    输出：["0->2","4->5","7"]
    解释：区间范围是：
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"
"""
def summaryRanges(nums):
    if len(nums) < 1:  return nums
    else:
        ans, t = [str(nums[0])], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == t + 1:
                t = nums[i]
                if i == len(nums) - 1:
                    ans[len(ans)-1] += '->%d' % t
            else:
                if str(t) != ans[len(ans)-1]:
                    ans[len(ans)-1] += '->%d' % t
                ans.append(str(nums[i]))
                t = nums[i]
        return ans

a = [0, 2, 3]
print(a, end='')
print(summaryRanges(a))