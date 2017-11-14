class Solution(object):
    def singleNumber(self, nums):
        """
                :type nums: List[int]
                :rtype: int
                """
        found_dict = {}
        for i in range(len(nums)):
            if nums[i] in found_dict:
                found_dict.pop(nums[i])
            else:
                found_dict[nums[i]] = 1

        return list(found_dict.keys())[0]

if __name__ == '__main__':
    solution = Solution()
    answer = solution.singleNumber([1, 3, 1, -1, 3])
    print(answer)
