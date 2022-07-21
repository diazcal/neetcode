"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


** Example 1 **
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

** Example 2 **
Input: nums = [3,2,4], target = 6
Output: [1,2]

** Example 3 **
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Couldn't find a solution without double for loop O(n^2) --> that's horrible
        """
        hash_values = {}
        for n in nums:
            hash_values[n] = 0
        for index, n in enumerate(hash_values.keys()):
            print(index, n)


input_list = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.two_sum(input_list, target))


class NeetSolution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # O(n + n)
        # I did this solution without watching the whole video. Afterwards I lernt you dont
        # need to initialize the hashmap and the result array either. You can return at real time.
        hash_set = {n: index for index, n in enumerate(nums)}
        result = []
        for index, n in enumerate(nums):
            difference_n = target - n
            if difference_n in hash_set.keys():
                if index == hash_set[difference_n]:
                    continue
                result.append(index)
        return result

    def two_sum_the_good_one(self, nums: list[int], target: int) -> list[int]:
        """
        time O(n)
        space O(n)
        """
        hash_map = {}
        for index, n in enumerate(nums):
            number_to_check = target - n
            if number_to_check in hash_map:
                return [hash_map[number_to_check], index]
            hash_map[n] = index


solution = NeetSolution()
print(solution.two_sum(input_list, target))
print(solution.two_sum_the_good_one(input_list, target))