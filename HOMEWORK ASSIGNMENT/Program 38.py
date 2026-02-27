# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column 
# to 0's. 
# You must do it in place. 
class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Step 1: Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Step 2: Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Step 3: Use first row/column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Set zeroes based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: Zero first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 6: Zero first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix


obj = Solution()
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

result = obj.setZeroes(matrix)
print(result)
