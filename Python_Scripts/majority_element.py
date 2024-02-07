"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    #O(n) time and O(n) space
    def majorityElement(self, nums: list[int]) -> int:
        target_len=len(nums)//2
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]=dict1[nums[i]]+1
            else:
                dict1[nums[i]]=1

        for key,value in dict1.items():
            if value>target_len:
                return key
            
    def majorityElement2(self, nums: list[int]) -> int:
        #O(n) time and O(1) space
        count=0
        element=0
        for num in nums:
            if count==0:
                element=num
            if element==num:
                count+=1
            else:
                count-=1
        return element