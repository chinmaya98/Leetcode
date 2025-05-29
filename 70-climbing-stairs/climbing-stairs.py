class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        one ,two = 1,1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one
        