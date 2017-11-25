class Solution(object):
    def majorityElement(self, nums):
        """
                :type nums: List[int]
                :rtype: int
                """
        import collections
        counts = collections.Counter(nums)
        print(counts.get)
        return max(counts.keys())


        """
        if nums is None or not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        threshold = len(nums) / 2

        times_dict = {}
        for n in nums:
            if n in times_dict:
                if times_dict[n] + 1 > threshold:
                    return n
                else:
                    times_dict[n] += 1
            else:
                times_dict[n] = 1
        """

if __name__ == '__main__':
    nums = [-3, -4, -3]
    print('origin strs: ' + ' '.join(str(p) for p in nums))

    solution = Solution()
    answer = solution.majorityElement(nums)

    print('Answer is: {}'.format(answer))
