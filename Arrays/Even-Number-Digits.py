# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(self, nums):

# initialize all variables 
    i = 0
    even_count = 0
    
    # traverse through the list
    for i in range(len(nums)):
        # convert each number into a string, then find the length of it
        # essentially finding the amount of digits in the nummber
        digits_num = len(str(nums[i]))
    
        # then dividing the length of each number by 2, to find the 
        # that the number has an even number of digits 
        if digits_num % 2 == 0:
            even_count += 1

    # then return the even count 
    return even_count

                
