class Solution(object):
    def maxProfit(self, prices):
        """
                :type prices: List[int]
                :rtype: int
                """
        import sys

        if prices is None or not prices:
            return 0

        max_diff = 0
        min_price = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif max_diff < prices[i] - min_price:
                max_diff = prices[i] - min_price

        return max_diff

    """
        def findMaxIndex(self, prices):
        max_price = prices[0]
        max_index = 0
        for i in len(prices):
            if max_price < prices[i]:
                max_price = prices[i]
                max_index = i

        return max_index

    def findMinIndex(self, prices):
        min_price = prices[0]
        min_index = 0
        for i in len(prices):
            if min_price > prices[i]:
                min_price = prices[i]
                min_index = i

        return min_index
    """

if __name__ == '__main__':
    solution = Solution()
    answer = solution.maxProfit([2, 4, 1])
    print(answer)

