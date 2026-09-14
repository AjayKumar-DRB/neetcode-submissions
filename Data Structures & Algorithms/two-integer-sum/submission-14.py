class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for i in range(len(nums)):
            if nums[i] in numHash:
                return [numHash[nums[i]], i]
            else:
                numHash[target-nums[i]] = i