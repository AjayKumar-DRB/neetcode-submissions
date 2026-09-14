class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        lst = []
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for i in set(nums):
            lst.append([i, count[i]])

        lst.sort(reverse = True, key=lambda x:x[1])

        for i in range(k):
            res.append(lst[i][0])

        return res

        