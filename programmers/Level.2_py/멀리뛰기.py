def coke(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2
    

    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n-1] % 1234567
print(coke(8))


# n	result
# 4	5
# 3	3

# 입출력 예 #2
# (2칸, 1칸)
# (1칸, 2칸)
# (1칸, 1칸, 1칸)