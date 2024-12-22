class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i
        num = 1
        while True:
            if num in table:
                num += 1
            else:
                return num
