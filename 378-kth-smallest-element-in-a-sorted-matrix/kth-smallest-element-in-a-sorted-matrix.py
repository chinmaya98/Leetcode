import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []
        
        # Push the first element of each row into the heap
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, col)
        
        # Extract the smallest k times
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        return heapq.heappop(min_heap)[0]  # k-th smallest element

# Example usage:
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
solution = Solution()
result = solution.kthSmallest(matrix, k)
print(result)
