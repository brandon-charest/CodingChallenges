""" 994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.
"""
from typing import List
from collections import deque
import unittest


class Oranges:

    def __init__(self):
        self.rotten = deque()
        self.visited = set()

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        time = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    self.rotten.append((i, j))
        while self.rotten:
            time += 1
            for _ in range(len(self.rotten)):
                row, col = self.rotten.popleft()

                if time > 0:
                    grid[row][col] = 2
                    fresh_oranges -= 1
                self.update_grid(grid, row, col)

        if fresh_oranges > 0:
            return -1
        return time if time >= 0 else 0

    def update_grid(self, grid, row, col):
        for dx, dy in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                if grid[dx][dy] == 1 and (dx, dy) not in self.visited:
                    self.rotten.append((dx, dy))
                    self.visited.add((dx, dy))


class TestGapInPrimes(unittest.TestCase):
    orange = Oranges()

    def should_return_valid_minute(self):
        orange = Oranges()
        test = [ [[2,1,1],[1,1,0],[0,1,1]], [[2,2,2,1,1]]]
        res = [4, 2]
        for i, t in enumerate(test):
            self.assertEqual(orange.orangesRotting(t), res[i])

    def should_return_zero(self):
        test = [[[0,2]], [[0]], [[]]]
        orange = Oranges()
        for t in test:
            self.assertEqual(orange.orangesRotting(t), 0)

    def should_return_minus_one(self):
        orange = Oranges()
        self.assertEqual(orange.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)


if __name__ == '__main__':
        unittest.main()
