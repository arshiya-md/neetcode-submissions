class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'}':'{', ']':'[', ')':'('}
        stack = []

        for c in s:
            if c in parentheses_map:
                top = stack.pop() if stack else '#'
                if parentheses_map[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack