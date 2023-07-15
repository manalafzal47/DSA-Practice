class Solution(object):
    def replaceElements(self, arr):
        # initialize max value with -1 because the last index will always get -1 
        max_value = -1
        
        # traverse through the array in reverse order, incrementing by 1 each time
        for i in range(len(arr) - 1, -1, -1):
            
            # initilize current element with current index in array traversal
            current_element = arr[i]
            
            # replace max value with the current element
            arr[i] = max_value
            
            # use the in-built function to replace the current element with the max value in-place
            max_value = max(max_value, current_element)
            
        return arr