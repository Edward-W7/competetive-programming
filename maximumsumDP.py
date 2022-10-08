N = int(input())
dp = []
for i in range(N+1):
    dp.append(0)


dp[1] = int(input())
for i in range(2, N+1):
    x = int(input())
    dp[i] = max(dp[i-1], x + dp[i-2])

print(dp[N])
