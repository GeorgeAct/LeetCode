class Solution:
    def firstUniqChar(self, s: str) -> int:
        tDict = {}
        for i in range(len(s)):
                tDict[s[i]] = i
        
        for i in range(len(s)):
            if tDict[s[i]] == i:
                return i
            tDict[s[i]] = i
            
        return -1