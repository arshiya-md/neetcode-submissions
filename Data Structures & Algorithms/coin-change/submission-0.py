class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        required_coins = [amount + 1] * (amount + 1)
        required_coins[0] = 0 # Amount 0 needs 0 coins

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    required_coins[amount] = min(required_coins[amount], 1 + required_coins[amount - coin]) # Current coin + (coins required for remaining amount = amount - coin)

        return required_coins[amount] if required_coins[amount] != amount + 1 else -1