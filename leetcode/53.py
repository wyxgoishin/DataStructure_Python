"""
题目描述：
    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
    要求时间复杂度为O(n)。
注意：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100
题解：
    1、动态规划法
    定义dp数组第i个元素的值为输入数组前i个数构成的数组的和与第i个数的最大值
    则dp[i+1] = max(dp[i] + nums[i], nums[i])
    要求的最大子数组和即为max(dp)
"""
def maxSubArray(nums):
    dp = [0] * (len(nums) + 1)
    dp[0] = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        maxSum = max(maxSum, dp[i])
    return maxSum


nums = [1, 2]
print(maxSubArray(nums))