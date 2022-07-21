"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


# Mi solución
def solution(nums):
    element_dict = {}
    for element in nums:
        if element not in element_dict:
            element_dict[element] = 1
            continue
        element_dict[element] += 1
    for key in element_dict.values():
        if key >= 2:
            return True
    return False


# num_list = [1, 2, 3, 1]
num_list = [1, 2, 3, 4]
# num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution(num_list))

"""
comentarios:
mi solución es sheit porque estoy interando dos veces y tengo además que iterar hasta el final
en vez de devolver en cuanto vea un duplicado. Había pensado en un set() pero descarté la idea
y no debería haberlo hecho. La solución de Neet lo utiliza
"""


class Solution:
    def contains_duplicate(self, nums):
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False


solution = Solution()
print(solution.contains_duplicate(num_list))