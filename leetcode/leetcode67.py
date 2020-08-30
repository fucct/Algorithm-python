class Solution67:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        length = min(len(a), len(b))
        carry = 0
        for idx in range(1, length + 1):
            index = idx * -1
            addNum = int(a[index]) + int(b[index]) + carry
            if addNum >1:
                addNum -= 2
                carry = 1
            else:
                carry = 0
            result = [str(addNum), *result]
        for i in range(idx+1, len(a)+1):
            index = i * -1
            addNum = int(a[index]) + carry
            if addNum >1:
                addNum -= 2
                carry = 1
            else:
                carry = 0
            result = [str(addNum), *result]
        for i in range(idx+1, len(b)+1):
            index = i * -1
            addNum = int(b[index]) + carry
            if addNum >1:
                addNum -= 2
                carry = 1
            else:
                carry = 0
            result = [str(addNum), *result]
        if carry == 1:
            result = [str(carry), *result]
        return "".join(result)

