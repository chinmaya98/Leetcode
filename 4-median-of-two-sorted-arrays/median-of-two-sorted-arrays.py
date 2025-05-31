class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merge = nums1+nums2
        merge.sort()
        t = len(merge)

        if t % 2 == 0:
            return (merge[t//2-1] + merge[t//2]) / 2.0
        else:
            return (merge[t//2])