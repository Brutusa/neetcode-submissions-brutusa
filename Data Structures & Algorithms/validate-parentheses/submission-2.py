class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")": "(", "}": "{", "]": "["}
        open_brackets = {"(", "{", "["}

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack or matches[char] != stack.pop():
                    return False

        return not stack

