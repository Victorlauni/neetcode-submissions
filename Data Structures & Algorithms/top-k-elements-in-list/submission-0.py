class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        # bucket sort
        sortingList = [None]*len(nums)
        for key, value in freqMap.items():
            if sortingList[value-1] == None:
                sortingList[value-1] = [key]
            else:
                sortingList[value-1].append(key)
        
        count = k
        result = []
        for ar in sortingList[::-1]:
            if ar is None: continue
            for ar2 in ar:
                if count > 0:
                    result.append(ar2)
                    count -= 1
        return result