class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        m = nums1+nums2
        m.sort()

        t = len(m)
        if t%2 == 0:
            return (m[t//2-1]+m[t//2])/2.0
        else:
            return (m[t//2])
        
        