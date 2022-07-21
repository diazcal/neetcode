"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Time and memory complexity O(n)


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
                continue
            if not stack:
                return False
            open_char = stack.pop()
            if ((open_char == '{' and char == '}')
                    or (open_char == '(' and char == ')')
                    or (open_char == '[' and char == ']')):
                continue
            else:
                return False
        if not stack:
            return True
        return False


s = ")("
solution = Solution()
print(solution.is_valid(s))


class NeetSolution:
    def is_valid(self, s: str) -> bool:
        stack = []
        close_map = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in close_map.keys():
                if stack and stack[-1] == close_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


s = "(([]{}))"
solution = NeetSolution()
print(solution.is_valid(s))