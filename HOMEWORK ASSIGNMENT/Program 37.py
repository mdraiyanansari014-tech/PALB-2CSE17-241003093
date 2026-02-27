# You are given a large integer represented as an integer array digits, where 
# each digits[i] is the ith digit of the integer. The digits are ordered from most significant 
# to least significant in left-to-right order. The large integer does not contain any 
# leading 0's. 
# Increment the large integer by one and return the resulting array of digits.
class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # If we exit loop, all digits were 9
        return [1] + digits


obj = Solution()
digits = [1, 2, 3]
result = obj.plusOne(digits)
print(result)
