class Solution:
    def addDigits(self, num: int) -> int:
        digits = (num//10) + (num%10)

        if digits > 9:
            return self.addDigits(digits)
        
        return digits