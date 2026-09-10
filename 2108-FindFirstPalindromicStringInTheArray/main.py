class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if len(word) == 1: return word
            length = round(len(word)/2)
            i = 0
            if len(word)%2 > 0: length-=1
            while length > i:
                if word[i] != word[-(i+1)]: i=length
                i+=1
                if i==length: return word
        return ""