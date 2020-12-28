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