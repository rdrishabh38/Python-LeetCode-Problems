from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> list[int]:
        compare_list = []
        len_of_nums = len(nums) - 1
        while len_of_nums >= 0:
            if nums[len_of_nums] in compare_list:
                nums.pop(len_of_nums)
            else:
                compare_list.append(nums[len_of_nums])
            len_of_nums = len_of_nums - 1
        print(nums)
        return nums


if __name__ == "__main__":
    solution = Solution()
    solution.removeDuplicates([1, 1, 2])
    solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])


