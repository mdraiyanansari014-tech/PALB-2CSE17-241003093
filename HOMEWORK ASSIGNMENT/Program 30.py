# Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and 
# columns is always odd. Return the median of the matrix. 
import bisect

class Solution:
    def matrix_median(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Minimum and maximum values
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        desired = (n * m) // 2

        while low < high:
            mid = (low + high) // 2

            # Count elements <= mid
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)

            if count <= desired:
                low = mid + 1
            else:
                high = mid

        return low

obj=Solution()
mat = [
 [1, 3, 5],
 [2, 6, 9],
 [3, 6, 9]
]
result=obj.matrix_median(mat)
print(result)
