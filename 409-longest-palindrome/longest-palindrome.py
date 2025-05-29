class Solution:
    def longestPalindrome(self, s: str) -> int:
        charset = set()
        result = 0

        for c in s:
            if c in charset:
                charset.remove(c)
                result +=2
            else:
                charset.add(c)
            
        if charset:
            result +=1
        return result
        