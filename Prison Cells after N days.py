class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        before=cells[:]
        cells[0]=0
        cells[7]=0
        for _ in range(7):
            for i in range(1,7):
                if before[i-1]==before[i+1]:
                    cells[i]=1
                else:
                    cells[i]=0
            before=cells[:]
        if (N//7)%2==1:
            for _ in range(N%7):
                for i in range(1,7):
                    if before[i-1]==before[i+1]:
                        cells[i]=1
                    else:
                        cells[i]=0
                before=cells[:]
            return cells
        else:
            for _ in range(7+N%7):
                for i in range(1,7):
                    if before[i-1]==before[i+1]:
                        cells[i]=1
                    else:
                        cells[i]=0
                before=cells[:]
            return cells
