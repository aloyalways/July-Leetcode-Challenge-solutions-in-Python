from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap=defaultdict(lambda:0)
        for i in nums:
            hashMap[i]+=1
        ans=[]
        for i in hashMap:
            if hashMap[i]==1:
                ans.append(i)
        return ans
