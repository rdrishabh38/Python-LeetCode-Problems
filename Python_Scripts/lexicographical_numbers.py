
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        
        # Helper function defined inside to easily access 'n' and 'result'
        def dfs(current_num):
            # If we exceed the limit, stop exploring this branch
            if current_num > n:
                return
            
            # 1. Add the valid number to our result
            result.append(current_num)
            
            # 2. Try to dive deeper by appending 0 through 9
            for i in range(10):
                next_num = current_num * 10 + i
                
                # Optimization: If next_num is already > n, we can break early 
                # because next_num + 1, next_num + 2, etc., will also be > n
                if next_num > n:
                    break
                    
                # 3. Recursively dive down the tree
                dfs(next_num)

        # The roots of our lexicographical tree are 1 through 9
        for i in range(1, 10):
            dfs(i)
            
        return result



if __name__ == "__main__":
    solution = Solution()
    print(solution.lexicalOrder(103)) 
    print(solution.lexicalOrder(2))   # Output: [1,2]