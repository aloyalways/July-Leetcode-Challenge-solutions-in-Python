class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(prices,i,bsc):
            if i>=len(prices):
                return 0
            if dp[i][bsc]!=float('inf'):
                return dp[i][bsc]
            if bsc==0:
                dp[i][bsc]=max(-1*prices[i]+solve(prices,i+1,1),solve(prices,i+1,0))
                return dp[i][bsc]
            elif bsc==1:
                dp[i][bsc]=max(prices[i]+solve(prices,i+1,2),solve(prices,i+1,1))
                return dp[i][bsc]
            else:
                dp[i][bsc]=solve(prices,i+1,0)
                return dp[i][bsc]
    
        dp=[[float('inf')]*3 for _ in range(len(prices)+1)]
        return solve(prices,0,0)
