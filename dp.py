def min_operations(n):
    dp = [0] * (n + 1)
    dp[1] = 0  # base case: 0 operations needed to reach 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1  # operation: subtract 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

n = int(input("Enter the number: "))
print("Minimum operations to reach 1:", min_operations(n))
