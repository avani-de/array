# LeetCode 121 - Best Time to Buy and Sell Stock

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# Example
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
