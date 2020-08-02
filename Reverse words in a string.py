class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(map(str,s.split(' ')))
        s=[i for i in s if i!=""]
        s=s[::-1]
        s=' '.join(s)
        return s
