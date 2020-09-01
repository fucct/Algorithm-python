class Solution125:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = list(filter(lambda ch: ch.isalnum(), list(s)))

        return filtered == filtered[::-1]
