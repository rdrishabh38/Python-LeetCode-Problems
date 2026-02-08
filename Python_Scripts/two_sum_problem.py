# 🧩 Problem 5: Two Sum
# The Problem: Given a list of integers nums and an integer target, return the indices of the two numbers in the list such that they add up to target.

# The Rules:

# You may assume that each input has exactly one solution.

# You may not use the same element twice.

# You can return the answer in any order.

# Examples:

# Input: nums = [2, 7, 11, 15], target = 9

# Output: [0, 1]

# Explanation: nums[0] (which is 2) + nums[1] (which is 7) equals 9.

# Input: nums = [3, 2, 4], target = 6

# Output: [1, 2]

# Explanation: nums[1] (which is 2) + nums[2] (which is 4) equals 6.

# Input: nums = [3, 3], target = 6

# Output: [0, 1]

# Explanation: nums[0] (which is 3) + nums[1] (which is 3) equals 6.

class two_sum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            if target - value in hash_map:
                key1 = hash_map[target - value]
                key2 = index
                return [key1, key2]
            else:
                hash_map[value] = index
        return []
    
if __name__ == "__main__":
    solver = two_sum()
    print(solver.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solver.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(solver.twoSum([3, 3], 6))          # Output: [0, 1]
                
                