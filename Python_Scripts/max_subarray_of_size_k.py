# Problem 3: Maximum Sum Subarray of Size K
# The Problem: Given a list of integers nums and an integer k, find the maximum sum of a contiguous subarray of size exactly k.

# Definitions:

# Subarray: A contiguous (unbroken) part of the list. For [1, 2, 3, 4], [2, 3] is a subarray, but [1, 3] is not.

# Size k: The subarray must contain exactly k elements.

# Examples:

# Input: nums = [2, 1, 5, 1, 3, 2], k = 3

# Output: 9

# Explanation: We look at all subarrays of size 3:

# [2, 1, 5] -> sum = 8

# [1, 5, 1] -> sum = 7

# [5, 1, 3] -> sum = 9

# [1, 3, 2] -> sum = 6

# The maximum sum is 9.

# Input: nums = [1, 9, -1, -2, 7, 3, -1, 2], k = 4

# Output: 13

# Explanation: The subarray [9, -1, -2, 7] has the maximum sum of 13.


class max_subarray_bruteforce:
    def max_subarray_of_k(self, nums: list[int], k: int) -> int:
        max_sum = -999999999
        left_pointer = 0
        right_pointer = k - 1
        current_sum = 0
        while right_pointer < len(nums):
            current_sum = 0
            for i in range(left_pointer, right_pointer + 1):
                current_sum = current_sum + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
                current_sum = 0
            left_pointer += 1
            right_pointer += 1
        return max_sum
    


class max_subarray_sliding_window:
    def max_subarray_of_k(self, nums: list[int], k: int) -> int:
        
        # 1. Handle edge case
        if len(nums) < k:
            return 0 # Or raise an error
            
        # 2. Get the sum of the FIRST window (from 0 to k-1)
        #    This is our starting point.
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # 3. Start the loop from the 'k'th element.
        #    This element is the FIRST one to *enter* the sliding window.
        for right_index in range(k, len(nums)):
            
            # 'right_index' is the new element entering the window
            # 'left_index' is the old element leaving the window
            left_index = right_index - k
            
            # 4. Slide the window:
            #    Add the new element on the right
            #    Subtract the old element on the left
            current_sum = current_sum + nums[right_index] - nums[left_index]
            
            # 5. Update the max_sum
            max_sum = max(max_sum, current_sum)
            
        return max_sum

if __name__ == "__main__":
    # solution = max_subarray_bruteforce()
    # print(solution.max_subarray_of_k([2, 1, 5, 1, 3, 2], 3))  # Output: 9
    # print(solution.max_subarray_of_k([1, 9, -1, -2, 7, 3, -1, 2], 4))  # Output: 13

    solution_sw = max_subarray_sliding_window()
    print(solution_sw.max_subarray_of_k([2, 1, 5, 1, 3, 2], 3))  # Output: 9
    print(solution_sw.max_subarray_of_k([1, 9, -1, -2, 7, 3, -1, 2], 4))  # Output: 13



