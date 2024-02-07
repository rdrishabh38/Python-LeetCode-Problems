from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length_of_nums = len(nums) - 1
        while length_of_nums >= 0:
            if nums[length_of_nums] == val:
                nums.pop(length_of_nums)
                length_of_nums = length_of_nums - 1
            else:
                length_of_nums = length_of_nums - 1
        # print(nums)
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    solution.removeElement([3, 2, 2, 3], 3)
    solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
