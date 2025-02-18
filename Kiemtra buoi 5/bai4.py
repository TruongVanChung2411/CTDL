def levenshtein_distance(token1, token2):
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

# Test case
print(levenshtein_distance("kitten", "sitting"))  # Output: 3
print(levenshtein_distance("hello", "hola"))  # Output: 2
print(levenshtein_distance("hi", "hello"))  # Output: 4
print(levenshtein_distance("you", "yu"))  # Output: 1