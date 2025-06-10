class Solution:
    def mergeAlternately(self, word1:str, word2:str) -> str:
        l = len(word1)
        m = len(word2)
        n = max(l,m)
        output = []

        for i in range(n):
            if i < l:
                output += word1[i]
            if i < m:
                output +=word2[i]
        return "".join(output)
