class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 0
        numSet = set(nums)
        for num in nums:
            if not num-1 in numSet:
                count = 1
                nextNum = num + 1
                while nextNum in numSet:
                    count += 1
                    nextNum = nextNum + 1
                maxNum = max(maxNum, count)
        return maxNum