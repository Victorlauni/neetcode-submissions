class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            wordArr = [c for c in word]
            wordArr.sort()
            hashKey = "".join(wordArr)
            if hashKey in group:
                group[hashKey].append(word)
            else:
                group[hashKey] = [word]
        return list(group.values())