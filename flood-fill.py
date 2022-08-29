## Problem Number 733 ###########
###### Time Complexity= O(n) ####
####### Space Complexity= O(n) ##
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev_color= image[sr][sc]
        if prev_color==color:
            return image
        def dfs(r,c):
            if image[r][c]==prev_color:
                image[r][c]=color
                if r>=1: dfs(r-1,c)
                if c>=1: dfs(r,c-1)
                if r<len(image)-1: dfs(r+1,c)
                if c<(len(image[0])-1): dfs(r,c+1)
        dfs(sr,sc)
        return image
        
