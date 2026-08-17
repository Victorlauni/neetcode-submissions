class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMap = dict()
        def insertToMap(isPos: bool, val: str):
            diff = 1 if isPos else -1
            if freqMap.get(val) == None:
                freqMap[val] = diff
            else:
                freqMap[val] += diff
        for i in range(len(s)):
            insertToMap(True, s[i])
            insertToMap(False, t[i])
        return all(x == 0 for x in freqMap.values())