class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Step 1: Check if L and R are in same order (ignoring '_')
        if start.replace("_", "") != target.replace("_", ""):
            return False

        # Step 2: Two pointers for non-'_' characters
        i = j = 0
        n = len(start)

        while i < n and j < n:
            # Skip _ in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            # Both reach end
            if i == n and j == n:
                return True

            # One reached end before other
            if i == n or j == n:
                return False

            # Characters should match
            if start[i] != target[j]:
                return False

            # Validate movement
            if start[i] == 'L' and i < j:
                return False  # L cannot move right
            if start[i] == 'R' and i > j:
                return False  # R cannot move left

            i += 1
            j += 1

        return True
