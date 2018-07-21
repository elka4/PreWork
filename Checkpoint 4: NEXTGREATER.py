"""
Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that
    j is minimum possible AND
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]


"""

#SOLUTION:


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        for i in range(len(A) - 1):
            j = i + 1

            while j < (len(A)):
                Found = False
                if A[j] > A[i]:
                    l.append(A[j])
                    Found = True
                    break

                else:
                    j += 1

            if Found == False:
                l.append(-1)
        l.append(-1)

        return (l)