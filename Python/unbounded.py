def rod_cutting(length, price, K):
    n = len(length)
    dp = [[0] * (K + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # Iterate over available rod lengths
        for j in range(0, K + 1):  # Iterate over rod length to cut
            if length[i - 1] <= j:  # If the piece length is <= remaining length
                dp[i][j] = max(
                    dp[i - 1][j],                     # Don't take this length
                    price[i - 1] + dp[i][j-length[i-1]]  # Take the piece (repeat allowed)
                )
            else:
                dp[i][j] = dp[i - 1][j]  # Can't take this length, move to next

        print(dp)
    
    print(dp[n][K])

# Example
length = [1, 2, 3]  # Available rod lengths
price = [3, 4, 6]   # Corresponding prices for each rod length
K = 5
rod_cutting(length, price, K)
