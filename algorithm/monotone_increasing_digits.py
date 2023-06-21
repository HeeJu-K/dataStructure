#738. Monotone Increasing Digits
### An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
### Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.


class Solution(object):
    def monotoneIncreasingDigits( n):
        """
        :type n: int
        :rtype: int
        """

        def monotone_digits(n):
            print("input", n)
            mark = 0
            digits = str(n)
            if len(digits) == 1 :
                return n
            
            for digit in range (len(digits)-1):
                if digits[digit] > digits[digit+1]:
                    print("digits here", digits)
                    mark = digit
                    break 
                print("digit", digit, len(digits)-2)
                if digit == len(digits)-2:
                    print("returned")
                    return n
            print("mark", mark)
            new_digit = int(digits[mark])-1
            if new_digit == 0 and mark == 0:
                return int("9"*(len(digits)-mark-1))
            else:
                print("before recursion", digits[:mark], "\nlong:",digits[:mark-1]+str(new_digit)+"9"*(len(digits)-mark-1))
                return monotone_digits(int(digits[:mark]+str(new_digit)+"9"*(len(digits)-mark-1)))

        output = monotone_digits(n)
        return output

    print("output", monotoneIncreasingDigits(332))