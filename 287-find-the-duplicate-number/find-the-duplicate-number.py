class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()
        result = 0

        for n in nums:
            while n in hashset:
                return n
            hashset.add(n)
        return  
        