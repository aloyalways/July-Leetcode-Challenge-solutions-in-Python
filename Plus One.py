class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(list(map(str,digits)))
        s=int(s)+1
        ans=list(map(str,str(s)))
        return ans
