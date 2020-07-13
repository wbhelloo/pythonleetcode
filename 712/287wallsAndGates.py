from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        从门开始找
        """

        def helper(col, row, val):
            if col < 0 or col >= cols or row < 0 or row >= rows:
                return
            if rooms[col][row] < val:
                return
            rooms[col][row] = val
            helper(col + 1, row, val + 1)
            helper(col - 1, row, val + 1)
            helper(col, row + 1, val + 1)
            helper(col, row - 1, val + 1)

        cols = len(rooms)
        rows = len(rooms[0])
        for i in range(cols):
            for j in range(rows):
                if rooms[i][j] == 0:
                    helper(i, j, 0)
        print(rooms)
        return None


if __name__ == '__main__':
    sol = Solution()
    sol.wallsAndGates(
        rooms=[[2147483647, -1, 0, 2147483647],
               [2147483647, 2147483647, 2147483647, -1],
               [2147483647, -1, 2147483647, -1],
               [0, -1, 2147483647, 2147483647]])
