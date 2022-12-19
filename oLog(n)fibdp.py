n = int(input())
dp = [-1 for i in range(n+1)]

def fib(n):
    if (n<=1):
        return n

    if (dp[n - 1] != -1):
        first = dp[n - 1]
    else:
        first = fib(n - 1)
    if (dp[n - 2] != -1):
        second = dp[n - 2]
    else:
        second = fib(n - 2)
    dp[n] = first + second

    return dp[n]
print(fib(n))
