# You are given an m x n integer matrix matrix with the following two  properties:
# • Each row is sorted in non-decreasing order. 
# • The first integer of each row is greater than the last integer of the previous row. 
# Given an integer target, return true if target is in matrix or false otherwise. 
# You must write a solution in O(log(m * n)) time complexity.
class Solution():
    def binarysearch_Matrix(matirx,type):
        # leftp
        m=len(matrix)
        n=len(matrix[0])
        left =0
        right=(m*n)-1
        while left<=right:
            mid=(left+right)//2
            row=mid//2
            col=mid%2
            midvalue=matrix[row][col]
            if midvalue== target:
                return True
            if midvalue< target:
                left=mid+1
            if midvalue== target:
                right=mid-1
        return false
      
