class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        numDict = {}
        for i in str(num):
            if i in numDict:
                count+= numDict[i]
                continue
            if num%int(i) > 0:
                numDict[i] = 0
                continue
            numDict[i] = 1
            count+=1
        return count