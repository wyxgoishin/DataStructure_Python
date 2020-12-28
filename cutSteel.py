steel_lengths = list(range(11))
steel_prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def maxPrice(steel_length):
    dp = [0] * (steel_length + 1)
    copy_len = min(len(dp), len(steel_lengths))
    dp[0:copy_len] = steel_prices[0:copy_len]
    for i in range(2, len(dp)):
        if i < len(steel_lengths):
            dp[i] = max(dp[j] + dp[i-j] for j in range(i//2+1))
        else:
            dp[i] = max(dp[j] + dp[i-j] for j in range(1, i//2+1))
    return dp[steel_length]


steel_length = 100
print("maxPrice of %dm steel is %d" %(steel_length, maxPrice(steel_length)))