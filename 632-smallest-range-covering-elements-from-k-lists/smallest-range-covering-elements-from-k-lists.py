from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums):
        min_heap = []  # Min-heap to track the smallest element across all lists
        max_value = float('-inf')  # Track the maximum element in the current range
        best_range = [-10**5, 10**5]  # Initialize with a large possible range

        # Step 1: Initialize the heap with the first element of each list
        for i, row in enumerate(nums):
            heappush(min_heap, (row[0], i, 0))  # (value, list_index, element_index)
            max_value = max(max_value, row[0])  # Update max_value

        # Step 2: Process the heap
        while min_heap:
            min_value, list_idx, ele_idx = heappop(min_heap)  # Get the smallest element
            
            # Update the best range if the new range is smaller
            if max_value - min_value < best_range[1] - best_range[0]:
                best_range = [min_value, max_value]

            # Step 3: Move to the next element in the current list
            if ele_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][ele_idx + 1]
                heappush(min_heap, (next_value, list_idx, ele_idx + 1))
                max_value = max(max_value, next_value)  # Update max_value
            else:
                break  # If any list is exhausted, stop as we can't cover all lists

        return best_range
