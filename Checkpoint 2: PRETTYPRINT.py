"""
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
Example 2:

Input: A = 3.
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.



"""

#Solution:

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):

        result = []
        n = ((2 * A) - 1)

        matrix = [[0 for i in range(n)] for j in range(n)]
        layers = A

        for i in range(layers):
            j = i
            if i == (layers - 1):
                matrix[i][i] = A
            else:

                while j <= n - 1 - i:
                    matrix[i][j] = A
                    matrix[j][n - 1 - i] = A
                    matrix[n - 1 - i][n - 1 - j] = A
                    matrix[n - 1 - j][i] = A
                    j += 1

            A -= 1
        for i in range(n):
            l = []
            for j in range(n):
                l.append(matrix[i][j])
            result.append(l)

        return result