class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(step):
            if step==n:
                return 1
            if step>n:
                return 0
            if dp[step]!=-1:
                return dp[step]
            else:
                dp[step]=solve(step+1)+solve(step+2)
                return dp[step]
        
        dp=[-1]*(n+1)
        ans=solve(0)
        return ans
