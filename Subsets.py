from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        for i in range(n+1):
            for elements in combinations(nums,i):
                ans.append(list(elements))
        return ans
