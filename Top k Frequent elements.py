from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map=defaultdict(lambda:0)
        for i in nums:
            Map[i]+=1
        heap=[]
        for i in Map:
            heapq.heappush(heap,(-Map[i],i))
        ans=[]
        for i in range(k):
            a=heapq.heappop(heap)[1]
            ans.append(a)
        return ans
