class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isPresent = set()
        for num in nums:
            if num in isPresent:
                return True
            isPresent.add(num)
        return False
         