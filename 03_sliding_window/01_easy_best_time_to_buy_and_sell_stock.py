"""
You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    def max_profit(self, prices: list[int]) -> int:
        left_pointer, right_pointer = 0, 1  # Left=buy, right=sell
        max_profit = 0

        while right_pointer < len(prices):
            # profitable transaction?
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, profit)  # between this two take the max
            else:
                left_pointer = right_pointer
            right_pointer += 1
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.max_profit(prices))
