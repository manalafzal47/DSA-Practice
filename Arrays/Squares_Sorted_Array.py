# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(self, nums):
    # first loop through each element
    i = 0
    new_array = [0] * len(nums)
    for i in range(len(nums)):
        # Then apply and find the square root of each number 
        new_array[i] = nums[i]*nums[i]
    
    # Then sort through the array using the python sort function        
    new_array.sort()

    return new_array        
