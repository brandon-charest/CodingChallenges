""" 1222. Queens That Can Attack the King
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens,
 and a pair of coordinates king that represent the position of the White King, return the coordinates of all
 the queens (in any order) that can attack the King.

Example:
[K,Q*,0,0,Q,0,0,0]
[Q*,0,0,0,0,0,0,0]
[0,0,0,0,Q*,0,0,0]
[0,0,0,Q,0,0,0,0]
[Q,0,0,0,0,0,0,0]
[0,0,0,0,0,0,0,0]
[0,0,0,0,0,0,0,0]
[0,0,0,0,0,0,0,0]

Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:
The queen at [0,1] can attack the king cause they're in the same row.
The queen at [1,0] can attack the king cause they're in the same column.
The queen at [3,3] can attack the king cause they're in the same diagonal.
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagonal as the king.
"""
from typing import List
BOARD_ROWS = 8
BOARD_COLS = 8


class QueensAttackKing:
    @staticmethod
    def queens_attack_king(queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        if len(queens) is 0 or len(king) is 0:
            return result
        # create set of queen x,y positions
        queens = set([(qx, qy) for qx, qy in queens])
        directions = [
            (-1, 0),  # ←
            (-1, 1),  # ↙
            (0, 1),   # ↓
            (1, 1),   # ↘
            (1, 0),   # →
            (1, -1),  # ↗
            (0, -1),  # ↑
            (-1, -1)  # ↖
        ]

        for dx, dy in directions:
            # reset king position each iteration
            x, y = king
            while 0 <= x < BOARD_ROWS and 0 <= y < BOARD_COLS:
                if (x, y) in queens:
                    result.append([x, y])
                    break
                x += dx
                y += dy
        return result


q = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
k = [0, 0]
r = QueensAttackKing.queens_attack_king(q, k)
print(r)
