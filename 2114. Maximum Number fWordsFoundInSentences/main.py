class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentenceIndex in sentences:
            spaces = sentenceIndex.count(" ")+1
            if spaces > maxWords:
                maxWords = spaces
        return maxWords