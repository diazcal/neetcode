"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up:
What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


class Solution:
    # O(n)
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result_num = 0
        for index, char in enumerate(s):
            result_num += ord(char)
            result_num -= ord(t[index])

        return not result_num


s_input = "anagram"
t_input = "anagrma"
solution = Solution()
print(solution.is_anagram(s_input, t_input))


# Neetcode soltions
class NeetSolution:
    def sol_1(self, s: str, t: str) -> bool:
        """
        Explanation:    we create two hashmaps per string and we count the times a char appears.
                        A afterwars we can compare both hashmaps and check if have the same
                        appearances.

        Complexity:     Time complexity: O(s+t)
                        Space complexity: O(s+t)

        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            """
            get returns None if don't exist, but if we pass 0 as
            second parameter it will return 0 instead. super naaaais trick :D 
            """
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True

    def sol_2(self, s: str, t: str) -> bool:
        """
        Explanation:    This solution is only for python and would not work in a job interview
                        most probably since is kind of "cheating".
                        You need to import Counter --> designed specially to count hashable objects.
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def sol_3(self, s: str, t: str) -> bool:
        """
        Explanation:    What if we are asked, can you solve this without extra memory? O(1) space complx.
                        For that case we could use a sorting algorithm. That would increase the
                        time complexity, good ones stay around O(log n) but that's to discuss with the 
                        interviewer
        """
        return sorted(s) == sorted(t)


neet_solution = NeetSolution()
print(neet_solution.sol_1(s_input, t_input))
print(neet_solution.sol_2(s_input, t_input))
print(neet_solution.sol_3(s_input, t_input))