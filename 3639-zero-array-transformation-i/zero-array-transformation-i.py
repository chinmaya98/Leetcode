class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        line = [0] * (n+1)

        for start, end in queries:
            line[start] +=1
            line[end+1] -=1
        
        for i in range(1,len(line)):
            line[i] += line[i-1]

        for i in range(n):
            if line[i] < nums[i]:
                return False
        return True
