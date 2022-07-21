"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left_p, right_p = 0, len(nums) - 1
        while left_p <= right_p:
            """
            In other languages but Python that might overflow because we could have
            2 large ints. the way to overcome this is to calculate the "distance"
            between them in this way:
            middle_p = left_p + ((right_p - left_p) // 2)
            """
            middle_p = (left_p + right_p) // 2
            if nums[middle_p] < target:
                left_p = middle_p + 1
            elif nums[middle_p] > target:
                right_p = middle_p - 1
            else:
                return nums[middle_p]
        return -1


solution = Solution()
print(solution.search([1, 2, 3, 4, 5], 5))