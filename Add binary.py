class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        a=a+b
        a=str(bin(a)[2:])
        return a
