from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows, num_cols = len(board), len(board[0])
        # ### using a set as storing a coordinate (r, c), and need to delete it
        visited = set()
        # visited = []

        def dfs(row, col, index): 
            #when reached to the end of the word, word is found
            if index == len(word):
                return True
            #invalid cases
            if (row >= num_rows or col >= num_cols or
                row < 0 or col < 0 or
                # [row, col] in visited or                
                (row, col) in visited or
                board[row][col] != word[index]): 
                
                return False
            
            #valid, found the next alphabet
            # visited.append([row, col])
            visited.add((row, col))
            res = ( dfs(row+1, col, index+1) or 
                    dfs(row-1, col, index+1) or
                    dfs(row, col-1, index+1) or
                    dfs(row, col+1, index+1))
            #at this point, either dfs returned True or False. when it is False, delete visited paths to start over
            # visited.remove([row, col])
            visited.remove((row, col))
            return res

        for r in range (num_rows):
            for c in range (num_cols):
                if dfs(r, c, 0): 
                    #if case satisfies when dfs returned true, meaning word found
                    return True 
        #did not find after
        return False


if __name__ ==  "__main__":
    solution = Solution()
    
    # res = solution.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    #                      word="ABCCED")
    res = solution.exist(board=[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], 
                         word="AAAAAAAAAAAAAAa")
    print(res)