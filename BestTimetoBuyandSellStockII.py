class Solution(object):
    def maxProfit(self, prices):
        """
                :type prices: List[int]
                :rtype: int
                """

        if not prices:
            return 0

        sum_profit = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                sum_profit += diff

        return sum_profit

if __name__ == '__main__':
    solution = Solution()
    answer = solution.maxProfit([2, 4, 1])
    print(answer)

