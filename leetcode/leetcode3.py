class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        result = []
        if len(s) == 1:
            return 1
        for idx in range(len(s)):
            if not result:
                result.append(s[idx])
                maxCount+=1
                continue
            if s[idx] in result:
                index = result.index(s[idx])
                result = result[index+1:len(result)]
                result.append(s[idx])
                maxCount = max(maxCount, len(result))
                continue
            else:
                result.append(s[idx])
                maxCount = max(maxCount, len(result))
        return maxCount