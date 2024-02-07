from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # logic is to traverse the nums1 and nums2 from -1 index, compare the elements and insert
        # bigger number at relevant position
        # Using two pointer approach

        # https://www.geeksforgeeks.org/two-pointers-technique/

        len_of_final_array = m + n - 1
        if m == 0:
            nums1 = nums2
        # elif n == 0:
        #     return nums1
        while m > 0 and n > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[len_of_final_array] = nums2[n-1]
                n = n - 1
            else:
                nums1[len_of_final_array] = nums1[m-1]
                m = m - 1
            len_of_final_array = len_of_final_array - 1
        print(nums1)


if __name__ == "__main__":
    solution = Solution()
    solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    solution.merge([1], 1, [], 0)
    solution.merge([0], 0, [1], 1)
