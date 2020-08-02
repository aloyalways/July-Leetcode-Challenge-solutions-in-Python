class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        p=len(word)
        
        def solve(r,c,pos):
            if pos>=p:
                return True
            elif 0<=r<m and 0<=c<n and board[r][c]==word[pos]:
                temp=board[r][c]
                board[r][c]=None
                if solve(r,c+1,pos+1) or solve(r,c-1,pos+1) or solve(r-1,c,pos+1) or solve(r+1,c,pos+1):
                    return True
                board[r][c]=temp
            return False
        
        for r in range(m):
            for c in range(n):
                if solve(r,c,0):
                    return True
        return False
