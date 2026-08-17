class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for it in strs:
            length = len(it)
            prefix = "#" + str(length) + "#"
            result += prefix
            result += it
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        cursor = 0
        result = []
        while cursor < len(s):
            lenStart = s.find("#", cursor) + 1
            lenEnd = s.find("#", cursor+1)
            strLen = int(s[lenStart:lenEnd])
            decoded = s[lenEnd+1:lenEnd+strLen+1]
            result.append(decoded)
            cursor = lenEnd+strLen+1
        return result