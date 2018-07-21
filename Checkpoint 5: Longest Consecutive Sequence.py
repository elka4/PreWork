"""

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""


#solution:


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        b = sorted(set((A)))
        a = 0
        count = 1
        for i in range(1, len(b)):
            if b[i] != (b[i - 1] + 1):
                a = i

            else:
                count = max(count, i - a + 1)
        return count

