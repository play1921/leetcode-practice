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

        candidates = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in candidates:
                print("find target!!! i={}, j={}".format(candidates[complement], i))
                return [candidates[complement], i]
            else:
                candidates[nums[i]] = i

        return []


if __name__ == "__main__":
    nums = [2, 5, 5, 10]
    s = Solution()
    answer = s.twoSum(nums, 10)
    print(answer)
