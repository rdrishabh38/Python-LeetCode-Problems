class Solution:
    def numOfIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfIslands([["1","1","1","1","0"],
                                 ["1","1","0","1","0"],
                                 ["1","1","0","0","0"],
                                 ["0","0","0","0","0"]]))  # Output: 1
    print(solution.numOfIslands([["1","1","0","0","0"],
                                 ["1","1","0","0","0"],
                                 ["0","0","1","0","0"],
                                 ["0","0","0","1","1"]]))  # Output: 3
