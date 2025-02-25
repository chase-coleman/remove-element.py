""""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
# k will be equal to the length of the array after removing the given value
# loop through the array, and if it matches the current index, remove it
class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) > 1:
            for num in nums[0:len(nums)+1]:
                if num == val:
                    nums.pop(nums.index(num))  
            k = len(nums)
        elif len(nums) == 1 and nums[0] == val or len(nums) == 0:
            k = 0
        elif len(nums) == 1 and nums[0] != val:
            k = len(nums)
        return k
    # This one fails Leetcode, because Leetcode wants the list modified in-place, and this creates a new list
    def filterFunc(self, nums, val):
        new_nums = list(filter(lambda x : x != val, nums))
        return new_nums


solution = Solution()
solution.filterFunc([12, 57, 33, 84, 19, 45, 67, 23, 12, 88,35, 92, 45, 33, 72, 19, 57, 84, 63, 27,45, 12, 57, 84, 19, 33, 68, 92, 45, 72,5, 33, 88, 45, 19, 23, 57, 12, 45, 77,63, 33, 57, 84, 19, 45, 67, 23, 12, 92,33, 88, 63, 45, 19, 57, 84, 33, 12, 45,67, 33, 12, 72, 45, 84, 19, 57, 33, 92,45, 63, 19, 33, 45, 57, 12, 84, 33, 45,19, 63, 33, 45, 57, 12, 84, 92, 45, 33,19, 27, 63, 72, 33, 45, 12, 19, 57, 88], 57)
# solution.filterFunc([24, 24, 24, 24, 24, 24, 24, 24,24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24,24, 24, 24, 24, 24], 24)
# solution.removeElement([24, 24, 24, 24, 24, 24, 24, 24,24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24,24, 24, 24, 24, 24], 24)
# solution.filterFunc([], 2)
# solution.removeElement([1,2,3,4,5,6,7,8,9], 0)

        




