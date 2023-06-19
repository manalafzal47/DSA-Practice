'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums 
which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution(object):
    def removeElement(self, nums, val):
        # create a new list to store all the elements other than val
        new_nums = []
        
        # check the elements of nums and then append the other elements 
        # in new_nums array 
        for num in nums:
            if num != val:
                new_nums.append(num)
        
        # update the original list with the new list
        nums[:] = new_nums
        
        # return modified array with val removed from nums
        return len(nums)
