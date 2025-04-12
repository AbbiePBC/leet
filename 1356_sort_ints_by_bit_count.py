
# 1356.

# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.

# DIFFICULTY: Easy

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/editorial/?source=submission-ac
# Could have used num.bit_count()
# Note that the number of 1 bits in an int is known as the Hamming Number

class Solution:

    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (Solution.getBitsAI(x), x))

    # This uses string manipulation and is slow
    # 14ms 17.84MB
    def getBits(v: int) -> int:
        b = format(v, 'b')
        return sum([1 for i in b if i == '1'])

    # Using bitwise operators will be more efficient
    # 11ms 17.80
    def getBitsBin(v: int) -> int:
        count = 0
        while v != 0:
            count += v & 1
            v >>= 1
        return count

    # 6ms 17.86
    def getBitsAI(v: int) -> int:
        count = 0
        while v:
            v &= (v - 1)  # Clear the least significant set bit
            #  Subtracting 1 from a number flips all the bits from the rightmost set bit to the end.
            # ANDing the original number with this result effectively clears the rightmost set bit.
            # The loop continues until all set bits are cleared.
            # This is better than above, because there are fewer iterations through the loop.
            count += 1
        return count


# Complexity analysis:
# TIME:
# sort is NlogN if using heapsort
# counting bits is dependent on the number of 1 bits, but *we are dealing with ints, which have a fixed size (31 bits)*
# => O(NlogN) for the sort and O(1) from bit count falls away
#
# SPACE:
# sort writes into new array of size N (O(N))
# bit comparison just uses fixed size (O(1))
# so, overall, O(N)


