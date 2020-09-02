class Solution38:
    def countAndSay(self, n: int) -> str:
        cache = ["1"]
        if n < 1:
            return ""
        if n == 1:
            return cache[0]
        for i in range(1, n):
            previous = cache[i - 1]
            cache.append(self.getNext(previous))
        print(cache)
        return cache[n - 1]

    def getNext(self, previous: str) -> str:
        stack = []
        result = ""
        for ch in previous:
            if not stack:
                stack.append(ch)
                continue
            if stack[-1] == ch:
                stack.append(ch)
                continue
            else:
                result += f"{len(stack)}{stack[-1]}"
                stack = [ch]
                continue
        if stack:
            result += f"{len(stack)}{stack[-1]}"
        return result
