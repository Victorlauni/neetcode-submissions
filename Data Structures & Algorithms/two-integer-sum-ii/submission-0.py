class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 1
        p2 = len(numbers)

        while p1 < p2:
            s = numbers[p1-1] + numbers[p2-1]
            if target == s:
                return [p1, p2]
            if target < s:
                p2 = p2 - 1
            else:
                p1 = p1 + 1
        return [p1, p2]