class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 25: return False
        temp = {}
        for char in range(len(sentence)):
            if sentence[char] not in temp:
                temp[sentence[char]] = 1
        
        if len(temp) == 26:
            return True
        else:
            return False