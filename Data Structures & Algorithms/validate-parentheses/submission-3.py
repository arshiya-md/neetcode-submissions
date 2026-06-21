class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []

        for p in s:
            if p not in parentheses_map:
                stack.append(p)
            else:
                if not stack or parentheses_map[p] != stack.pop():
                    return False
                    
        return True if not stack else False
