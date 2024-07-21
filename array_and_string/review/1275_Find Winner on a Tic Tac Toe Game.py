"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        board = [[0] * n for _ in range(n)]

        player = 1
        for row, col in moves:
            board[row][col] = player

            if sum(board[row]) == player * 3:
                return "A" if player == 1 else "B"

            col_sum = 0
            for i in range(n):
                col_sum += board[i][col]
            if col_sum == player * 3:
                return "A" if player == 1 else "B"

            if row == col:
                diag_sum = 0
                for i in range(n):
                    diag_sum += board[i][i]
                if diag_sum == player * 3:
                    return "A" if player == 1 else "B"

            if row + col == n - 1:
                ant_diag_sum = 0
                for i in range(n):
                    ant_diag_sum += board[i][n-1-i]
                if ant_diag_sum == player * 3:
                    return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == n*n else "Pending"   