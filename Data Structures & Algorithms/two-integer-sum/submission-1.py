class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keyToIndex = {}
        for ind, num in enumerate(nums):
            if num in keyToIndex:
                keyToIndex[num].append(ind)
            else:
                keyToIndex[num] = [ind]
        
        for ind, num in enumerate(nums):
            looking = target - num
            if looking in keyToIndex:
                for key in keyToIndex[looking]:
                    if key == ind:
                        continue
                    else:
                        if (ind > key):
                            return [key, ind]
                        else:
                            return [ind, key]
        return []