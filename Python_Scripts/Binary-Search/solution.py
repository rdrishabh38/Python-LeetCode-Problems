from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))
