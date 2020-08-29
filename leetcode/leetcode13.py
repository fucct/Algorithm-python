class Solution13:
    def romanToInt(self, s: str) -> int:
        main = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sub = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        result = 0

        for key in list(sub.keys()):
            result += s.count(key) * sub.get(key)
            s = s.replace(key, "")

        for key in list(main.keys()):
            result += s.count(key) * main.get(key)
            s = s.replace(key, "")

        return result