class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList()
        l = 0
        result = 0

        for r in range(len(nums)):
            sl.add(nums[r])
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[l])
                l +=1
            result += r-l+1
        return result