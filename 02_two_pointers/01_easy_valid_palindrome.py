"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
* Example 1
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

* Example 2
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

* Example 3
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Not the most optimal because I traverse the whole string twice:
            1. To create the new string without the alfanumertic
            2. To compare all the characters of the string from the begining and from the end

        In the solution from Neet he does the isalnum() at the same time he is traversing
        and only traverses half (because the other half is the palindrome that we already
        traversed)
        """
        s = "".join(char.lower() for char in s if char.isalnum())
        for index, char in enumerate(s):
            if char != s[-index - 1]:
                return False
        return True


input_str1 = "A man, a plan, a canal: Panama"
input_str2 = "race a car"
input_str3 = " "

solution = Solution()
print(solution.isPalindrome(input_str1))


class NeetSolution:
    def is_palindrome_sol_1(self, s: str) -> bool:
        """
        "Cheating" solution:    1.  Using the isalnum()
                                2.  Using extra memory because we are building the new string 
                                    to compare it with the one we built after cleaning the
                                    alfanumeric characters.
        """
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]     # Python for string in reverse order

    def is_palindrome_sol_2(self, s: str) -> bool:
        """
        This is a O(1) solution to be super memory performant.
        In this case we are going to traverse the string from the end and the
        begining at the same time and compare both.

        Extra effort: we will build our own alfanumeric function to check if the char
        is a letter o number.
        """
        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            while left_index < right_index and not self.alpahnum(s[left_index]):
                left_index += 1
            while left_index < right_index and not self.alpahnum(s[right_index]):
                right_index -= 1
            if s[left_index].lower() != s[right_index].lower():
                return False
            left_index, right_index = left_index + 1, right_index - 1
        return True

    def alpahnum(self, c: str) -> bool:
        """
        Custom alphanumeric checker
        """
        return (ord('A') <= ord(c) <= ord('Z')
                or ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9'))


solution = NeetSolution()
print(solution.is_palindrome_sol_1(input_str1))
print(solution.is_palindrome_sol_2(input_str1))
