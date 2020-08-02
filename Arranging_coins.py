class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        ans=0
        while ans<=n:
            i+=1
            ans+=i
        if ans==n:
            return i
        return i-1
