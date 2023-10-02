"""
Approach: Bit manipulation
Starting from rightmost bit, append each bit at a value then leftshift to reverse. At last, leftshift (32 - length) bits to get the final result

do & operation with 1 -> get the rightmost bit
Operation is done when number is smaller than 1
"""
class Solution:
    def operate(self, right_bit, store_bits, length):
        if right_bit < 1:
            return store_bits << (32 - length)
        return self.operate(right_bit >> 1, (store_bits << 1 | right_bit & 1), length + 1)

    def reverseBits(self, n: int) -> int:
        return self.operate(n, 0, 0)
        