# Given an array arr[] of positive integers. Return true if all the array elements are 
# palindrome otherwise, return false. 
class Solution():
    def is_palindrome(self, num):
        return str(num) == str(num)[::-1]

    def all_palindromes(self, arr):
        for num in arr:
            if not self.is_palindrome(num):
                return False
        return True


obj = Solution()
arr = [111, 222, 333, 444, 555]
result = obj.all_palindromes(arr)
print(result)
