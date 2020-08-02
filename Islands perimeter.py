class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=0
        for i in range(n):
            m=max(m,len(grid[i]))
            grid[i]=[0]+grid[i]+[0]
        grid=[[0]*(m+2)]+grid+[[0]*(m+2)]
        perimeter=0
        for i in range(n+2):
            for j in range(m+2):
                if grid[i][j]==1:
                    if grid[i+1][j]==0:
                        perimeter+=1
                    if grid[i-1][j]==0:
                        perimeter+=1
                    if grid[i][j+1]==0:
                        perimeter+=1
                    if grid[i][j-1]==0:
                        perimeter+=1
        return perimeter
