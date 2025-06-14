class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashset = set()

        for i in range(len(s)):
            if s[i] in hashset:
                return s[i]
            hashset.add(s[i])
        return