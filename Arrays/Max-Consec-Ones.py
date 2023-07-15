# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(self, nums):
    # Go through each number in array; iterate through each number
    max_count = 0
    overall_max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1 :
            max_count+=1
            overall_max_count = max(max_count, overall_max_count)
            
        elif nums[i] == 0:
            max_count=0

    return overall_max_count
