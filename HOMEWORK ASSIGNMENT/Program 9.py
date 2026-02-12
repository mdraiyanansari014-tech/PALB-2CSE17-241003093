#  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
class Solution:
    def returnindice(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


obj=Solution()
nums = [2,11,7,11,15]
target = 9 
res=obj.returnindice(nums,target)
print(res)
