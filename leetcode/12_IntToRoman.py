"""
Tip: Utilize boundaries of testcase
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        res = ""
        res += thousands[num//1000]
        num %= 1000
        res += hundreds[num//100]
        num %= 100
        res += tens[num//10]
        num %= 10
        res += ones[num//1]
        return res