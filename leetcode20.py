class Solution20:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in list(parentheses.keys()):
                stack.append(ch)
            elif ch in list(parentheses.values()):
                try:
                    head = stack.pop()
                    if parentheses.get(head) != ch:
                        return False
                except:
                    return False
        if len(stack) != 0:
            return False
        return True
