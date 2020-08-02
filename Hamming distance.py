class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=str(bin(x)[2:])
        y=str(bin(y)[2:])
        if len(x)>len(y):
            y="0"*(len(x)-len(y))+y
        else:
            x="0"*(len(y)-len(x))+x
        hamming=0
        for i in range(len(x)):
            if x[i]!=y[i]:
                hamming+=1
        return hamming
