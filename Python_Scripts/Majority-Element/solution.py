from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        length_of_nums = len(nums)

        if length_of_nums % 2 == 0:
            majority_element_occurence_count = length_of_nums//2
        else:
            majority_element_occurence_count = (length_of_nums // 2) + 1

        nums_element_count_tracker_dict = {}
        most_right_index_of_nums = length_of_nums - 1
        while most_right_index_of_nums >= 0:
            if nums[most_right_index_of_nums] in nums_element_count_tracker_dict.keys():
                nums_element_count_tracker_dict[nums[most_right_index_of_nums]] = nums_element_count_tracker_dict[nums[most_right_index_of_nums]] + 1
            else:
                nums_element_count_tracker_dict[nums[most_right_index_of_nums]] = 1
            most_right_index_of_nums = most_right_index_of_nums - 1

        maxkey = max(zip(nums_element_count_tracker_dict.values(), nums_element_count_tracker_dict.keys()))[1]
        # print(maxkey)
        return maxkey


if __name__ == "__main__":
    solution = Solution()
    solution.majorityElement([3, 2, 3])
    solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
