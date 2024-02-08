from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        compare_dict = {}
        len_of_nums = len(nums) - 1
        while len_of_nums >= 0:
            if nums[len_of_nums] in compare_dict.keys() and compare_dict[nums[len_of_nums]] == 2:
                nums.pop(len_of_nums)
            else:
                if nums[len_of_nums] not in compare_dict.keys():
                    compare_dict[nums[len_of_nums]] = 1
                else:
                    compare_dict[nums[len_of_nums]] = 2
            len_of_nums = len_of_nums - 1
        # print(nums)
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    solution.removeDuplicates([1, 1, 1, 2, 2, 3])
    solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
