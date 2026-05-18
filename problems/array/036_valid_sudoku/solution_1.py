from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set()  for _ in range(3)]  for _ in range(3)]

        for i in range(9):
            for j in range(9):

                try:
                    num = int(board[i][j])

                    if num in rows[i] or num in cols[j] or num in squares[i // 3][j // 3]:
                        return False

                    else:
                        rows[i].add(num)
                        cols[j].add(num)
                        squares[i // 3][j // 3].add(num)
                
                except:
                    continue
        
        return True