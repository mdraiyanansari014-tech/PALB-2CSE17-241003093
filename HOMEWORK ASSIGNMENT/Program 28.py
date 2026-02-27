# Matrix mxn given , traverse the matrix in a spiral form and push all elements into result[]
# You are given a rectangular matrix mat[][] of size n x m, and your task is to return an 
# array while traversing the matrix in spiral form. 
class Solution:
    def spiral_traverse(self, matrix):
        if not matrix or not matrix[0]:
            return []
        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            # top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                # right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                # bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

obj = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]
res = obj.spiral_traverse(matrix)
print(res)
