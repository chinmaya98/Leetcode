class Solution:
    def longestPalindrome(self, s: str) -> int:
        charSet = set()
        output = 0

        for c in s:
            if c in charSet:
                charSet.remove(c)
                output +=2
            else:
                charSet.add(c)
        
        if charSet:
            output +=1
        
        return output
        