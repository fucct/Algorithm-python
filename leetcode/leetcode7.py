class Solution7:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        string = str(x)
        split = [char for char in string]
        if '-' in split:
            split = split[1:]
            split.reverse()
            nonZeroIdx = 0
            for letter in split:
                if letter != '0':
                    break
                else:
                    nonZeroIdx += 1
            split = split[nonZeroIdx:]
            result = int(''.join(split)) * -1
            if result < -2**31:
                return 0
            return result
        else:
            split.reverse()
            nonZeroIdx = 0
            for letter in split:
                if letter != '0':
                    break
                else:
                    nonZeroIdx += 1
            split = split[nonZeroIdx:]

            result = int(''.join(split))
            if result > 2**31-1:
                return 0
            return result
