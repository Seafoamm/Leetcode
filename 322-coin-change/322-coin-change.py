class Solution:
    

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        if not coins:
            return -1
        coins.sort()
        if coins[0] > amount:
            return -1
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin > 0:
                    # print(i, coin)
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        # print(dp)
        return dp[amount] if dp[amount] < float('inf') else -1