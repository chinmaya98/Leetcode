class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        pfSum = {0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += pfSum.get(diff,0)
            pfSum[curSum] = 1 + pfSum.get(curSum,0)
        return res
        
        
        