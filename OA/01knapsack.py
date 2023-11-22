
def knapsack_01(w, v, max_w):
# w for weights, v for values, max_w for maximum capacity of the knapsack
	n = len(v)
	dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]

	for i in range (1, n+1):
		for j in range (1, max_w+1):
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1]) if j>=w[i-1] else dp[i-1][j]
	return dp[n][max_w]

def print_matrix(a):
    print("here")
    for row in a:
        print(row, "\n")

# Example usage:
weights = [4, 2, 7, 1, 2]
values = [270, 142, 450, 124, 189]
knapsack_capacity = 10

max_value = knapsack_01(weights, values, knapsack_capacity)
print("Maximum value that can be obtained:", max_value)
