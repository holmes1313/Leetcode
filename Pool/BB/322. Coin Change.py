class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dynamic programming approach is efficient for problems involving combinations or sums
        # Initialize dp array where dp[i] represents the minimum coins to make amount i
        dp = [float('inf')] * (amount + 1)
        # base case
        dp[0] = 0
        for coin in coins:
            # Update dp values for all amounts from coin to amount
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still inf, it means we cannot make the amount with the given coins
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_wrong(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        count = 0
        i = 0
        while amount > 0 and i < len(coins):
            if amount >= coins[i]:
                count += amount // coins[i]
                amount %= coins[i]
            i += 1

        if amount != 0:
            return -1
        else:
            return count

