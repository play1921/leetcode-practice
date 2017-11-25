class Solution(object):
    def climbStairs(self, n):
        """
                :type n: int
                :rtype: int
                """
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        if n == 1 or n == 2:
            return n

        index = 2
        smaller = 1
        larger = 2
        for i in range(3, n+1):
            temp = larger
            larger = smaller + temp
            smaller = temp

        return larger



if __name__ == '__main__':
    input_num = 35
    print("input: {}".format(input_num))
    solution = Solution()
    answer = solution.climbStairs(input_num)
    print("answer: {}".format(answer))

