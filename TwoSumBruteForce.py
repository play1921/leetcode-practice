class Solution(object):
    def twoSum(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
        if not isinstance(nums, list):
            print("nums is not a list.")
            return []

        if not isinstance(target, int):
            print("target is not an int.")
            return []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print("find target!!! i={}, j={}".format(i, j))
                    return [i, j]

        return []


if __name__ == "__main__":
    nums = [2, 5, 5, 10]
    s = Solution()
    answer = s.twoSum(nums, 10)
    print(answer)
