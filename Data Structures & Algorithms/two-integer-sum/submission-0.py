class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedInd = {}
        for ind, num in enumerate(nums):
            reverseSearch = target - num
            if visitedInd.get(reverseSearch) != None:
                return [visitedInd.get(reverseSearch), ind]
            else:
                visitedInd[num] = ind if visitedInd.get(num) == None else visitedInd.get(num)