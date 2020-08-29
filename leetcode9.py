import functools


class Solution9:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        split_list = [char for char in string]
        reversed_list = split_list[:]
        reversed_list.reverse()

        return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, split_list, reversed_list), True)
