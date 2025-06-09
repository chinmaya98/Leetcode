class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        heap= []
        boarders = [0] * (len(nums)+1)
        q = 0
        operations = 0

        for index, num in enumerate(nums):
            operations += boarders[index]
            while q < len(queries) and queries[q][0] == index:
                heappush(heap, -queries[q][1])
                q +=1
            while operations < num and heap and -heap[0] >= index:
                operations +=1
                boarders[-heappop(heap)+1] -=1
            if operations < num:
                return -1
        return len(heap)
