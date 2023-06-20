'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        # create a new array 
        newarray = []
        # traverse through nums array 
        for num in range(len(nums)):
            # check if the array is at the last element, or check if the current element 
            # is the same as the element to the right, if it isn't, then append it to the new list
            if num == len(nums)-1 or nums[num] != nums[num+1]:
                newarray.append(nums[num])
        
        # replaces the elements of nums with new array, modifying the array in place
        nums[:] = newarray
        
        # return modified nums array 
        return len(nums)
