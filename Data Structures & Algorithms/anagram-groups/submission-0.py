class Solution:
    def calHash(self, string: str) -> str:
        return hash("".join(sorted(string)))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}
        for string in strs:
            stringHash = self.calHash(string)
            if stringHash in groupMap:
                groupMap[stringHash].append(string)
            else:
                groupMap[stringHash] = [string]
        result = []
        for key in list(groupMap):
            result.append(groupMap[key])
        return result