# 70. Climbing Stairs
# Attempted
# Easy
# Topics
# conpanies iconCompanies
# Hint

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

 

# Constraints:

#     1 <= n <= 45



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            for _ in range(2, n):
                c = a+b
                a=b
                b=c
            return c

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))  # Output: 1
    print(solution.climbStairs(2))  # Output: 2
    print(solution.climbStairs(3))  # Output: 3
    print(solution.climbStairs(4))  # Output: 5
    print(solution.climbStairs(5))  # Output: 8
    print(solution.climbStairs(6))  # Output: 13
    print(solution.climbStairs(7))  # Output: 21