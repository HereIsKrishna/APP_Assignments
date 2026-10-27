def lcs(X, Y):
    # Find the lengths of both sequences
    m = len(X)
    n = len(Y)

    # Create a DP table filled with zeros
    # Rows represent X and columns represent Y
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Traverse both sequences character by character
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters match, add 1 to the diagonal value
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If characters do not match, take the maximum
            # of the value above and the value on the left
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # Return the length of the LCS from the last cell
    return dp[m][n]


# Accept the first sequence from the user
X = input("Enter first sequence: ")

# Accept the second sequence from the user
Y = input("Enter second sequence: ")

# Calculate the length of the LCS
result = lcs(X, Y)

# Display the final result
print("Length of LCS:", result)