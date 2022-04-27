class Solution:
    def exist(self, board, word):
        
        if not word:
            return True
        if not board:
            return False
        
        m=len(board)
        n=len(board[0])
        w=len(word)-1
        
        
        def dfs(i,j,k):
            if (i<0) or (i>=m) or (j<0) or (j>=n):
                return False
            
            if board[i][j] != word[k]:
                return False
            
            if board[i][j]=='#':
                return False
            
            if k==w:
                return True
            
            tmp = board[i][j]
            board[i][j]='#'
            
            k +=1
            
            for x,y in ((+1,0),(-1,0),(0,-1),(0,+1)):
                if dfs(i+x,j+y,k):
                    return True
            board[i][j]=tmp
            return False         
        
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
