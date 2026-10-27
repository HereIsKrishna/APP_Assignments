
# Knapsack Problem using Dynamic Programming

# Function for Bottom-Up approach
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create a DP table initialized with zeros
    # dp[i][w] stores the maximum value using first i items
    # with a maximum weight capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Process each item one by one
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # If the item's weight is within the capacity
            if weights[i - 1] <= w:

                # Choose the maximum of including or excluding the item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)

            else:
                # Item cannot be included due to its weight
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value for all items and given capacity
    return dp[n][capacity]


# Function for Top-Down approach
def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Create a memoization table to store calculated results
    memo = {}

    # Recursive function to solve smaller subproblems
    def solve(i, w):

        # If no items remain or capacity becomes zero
        if i == n or w == 0:
            return 0

        # Return the stored result if already calculated
        if (i, w) in memo:
            return memo[(i, w)]

        # If the current item is too heavy, skip it
        if weights[i] > w:
            memo[(i, w)] = solve(i + 1, w)

        else:
            # Calculate value by including the current item
            include = values[i] + solve(i + 1, w - weights[i])

            # Calculate value by excluding the current item
            exclude = solve(i + 1, w)

            # Store the maximum value in the memo table
            memo[(i, w)] = max(include, exclude)

        # Return the best value for this subproblem
        return memo[(i, w)]

    # Start with the first item and full capacity
    return solve(0, capacity)


# Input items
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

# Display results from both approaches
print("Bottom-Up Maximum Value:",
      knapsack_bottom_up(weights, values, capacity))

print("Top-Down Maximum Value:",
      knapsack_top_down(weights, values, capacity))
