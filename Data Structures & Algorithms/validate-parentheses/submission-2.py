class Solution:
    def isValid(self, s: str) -> bool:
        records = []
        for gg in s:
            if gg == '[' or gg == '(' or gg == '{':
                records.append(gg)
            else:
                if len(records) <= 0:
                    return False
                tmp = records.pop()
                if (gg == ']' and tmp == '[') \
                or (gg == '}' and tmp == '{') \
                or (gg == ")" and tmp == '('):
                    continue
                else:
                    return False
        return len(records) == 0
            