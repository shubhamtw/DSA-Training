class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        opening_brackets = set(["(", "[", "{"])

        for c in s:
            if c in opening_brackets:
                stack.append(c)
            elif stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
A
        if stack:
            return False
        else:
            return True







