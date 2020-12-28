"""
题目描述：
    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
    要求时间复杂度为O(n)。
注意：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100
"""
def maxSubArray(nums):
    dp = [0] * len(nums)
    maxSum = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        maxSum = max(maxSum, dp[i])
    return maxSum


nums = [20, -20, -100, 19]
print(maxSubArray(nums))